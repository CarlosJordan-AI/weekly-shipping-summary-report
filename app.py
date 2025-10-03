import argparse, os, sqlite3, random
from datetime import datetime, timedelta
import pandas as pd

DB_PATH = os.path.join(os.path.dirname(__file__), "app.db")
REPORT_SQL_PATH = os.path.join(os.path.dirname(__file__), "report.sql")

def seed():
    # fresh DB
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # schema mirrors your first report (Orders ↔ Packages)
    cur.executescript("""
    DROP TABLE IF EXISTS "order";
    DROP TABLE IF EXISTS "shippackage";

    CREATE TABLE "order"(
        id INTEGER PRIMARY KEY,
        xid TEXT,
        CustomPartnerId TEXT,
        SortedOnUtc TEXT,             -- ISO8601
        TotalWeightLbs REAL,
        ShippingBase REAL,
        ShippingAmount REAL,
        FactoryId INTEGER,
        ShippingPriority INTEGER,
        IsInvoiced INTEGER,
        IsShippingInvoiced INTEGER,
        ShippingCarrier TEXT,
        InvoiceWeek TEXT
    );

    CREATE TABLE "shippackage"(
        id INTEGER PRIMARY KEY,
        OrderId INTEGER,
        TrackingNumber TEXT,
        FOREIGN KEY(OrderId) REFERENCES "order"(id)
    );
    """)

    random.seed(11)
    carriers = ["DHLGM", "UPS", "FedEx"]
    partners = ["printify", "teepublicvip", "brewcity", "acme"]
    start = datetime(2023, 11, 1)

    orders, pkgs = [], []
    oid, pid = 1, 1

    # ~5 months of data; 1–6 orders per day; 1–3 packages per order
    for day in range(0, 160):
        d = start + timedelta(days=day)
        for _ in range(random.randint(1, 6)):
            partner = random.choice(partners)
            factory = random.choice([1, 2, 3])
            carrier = random.choice(carriers)
            is_inv  = int(random.random() < 0.85)
            is_ship = int(random.random() < 0.8)
            wt      = round(random.uniform(0.2, 25.0), 2)
            base    = round(random.uniform(2.00, 20.00), 2)
            amt     = round(base + random.uniform(0.5, 6.0), 2)
            prio    = random.choice([1, 2, 3])
            iw      = f"{d.isocalendar().year}-W{d.isocalendar().week:02d}" if is_inv else None

            xid = f"{d.strftime('%y%m%d')}{oid:06d}"
            orders.append((oid, xid, partner, d.isoformat(), wt, base, amt,
                           factory, prio, is_inv, is_ship, carrier, iw))

            for p in range(random.randint(1, 3)):
                tracking = f"{carrier}-{oid:06d}-{p+1:02d}"
                pkgs.append((pid, oid, tracking))
                pid += 1

            oid += 1

    cur.executemany("""
        INSERT INTO "order"(id, xid, CustomPartnerId, SortedOnUtc, TotalWeightLbs, ShippingBase,
                            ShippingAmount, FactoryId, ShippingPriority, IsInvoiced,
                            IsShippingInvoiced, ShippingCarrier, InvoiceWeek)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, orders)

    cur.executemany("""
        INSERT INTO "shippackage"(id, OrderId, TrackingNumber) VALUES (?, ?, ?);
    """, pkgs)

    conn.commit()
    conn.close()
    print("Seeded fake data into", DB_PATH)

def run_report(start, factory=None, partner="", carrier="", out_csv=None):
    if not os.path.exists(DB_PATH):
        seed()

    conn = sqlite3.connect(DB_PATH)
    with open(REPORT_SQL_PATH, "r") as f:
        sql = f.read()
    params = {
        "start":   start,
        "factory": factory,
        "partner": partner or "",
        "carrier": carrier or ""
    }
    df = pd.read_sql_query(sql, conn, params=params)
    conn.close()

    # Derived metrics (done in Python for SQLite simplicity)
    if not df.empty:
        df["ShippingMarkup"] = df["ShippingAmount"] - df["ShippingBase"]
        # Averages per order/package (avoid division by zero)
        df["AvgShipAmtPerOrder"]   = (df["ShippingAmount"] / df["Orders"]).round(2)
        df["AvgShipAmtPerPackage"] = (df["ShippingAmount"] / df["Packages"]).round(2)

    print("\n=== Parameters ===")
    print(params)

    print("\n=== Sample Rows ===")
    print(df.head(10).to_string(index=False))

    print("\n=== Grand Totals (all groups) ===")
    if df.empty:
        print("No rows.")
    else:
        g = {
            "Orders":          int(df["Orders"].sum()),
            "Packages":        int(df["Packages"].sum()),
            "ShippingBase":    float(df["ShippingBase"].sum()),
            "ShippingAmount":  float(df["ShippingAmount"].sum()),
            "ShippingMarkup":  float(df["ShippingMarkup"].sum())
        }
        print(g)

    if out_csv:
        df.to_csv(out_csv, index=False)
        print(f"\nSaved CSV to {out_csv}")

def main():
    parser = argparse.ArgumentParser(description="Weekly shipping summary report.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("seed", help="Create/refresh SQLite DB with fake data.")

    pr = sub.add_parser("report", help="Run weekly summary.")
    pr.add_argument("--start", default="2023-12-01")
    pr.add_argument("--factory", type=int, default=None)
    pr.add_argument("--partner", default="")
    pr.add_argument("--carrier", default="")
    pr.add_argument("--out", dest="out_csv")

    args = parser.parse_args()
    if args.cmd == "seed":
        seed()
    elif args.cmd == "report":
        run_report(args.start, args.factory, args.partner, args.carrier, args.out_csv)

if __name__ == "__main__":
    main()
