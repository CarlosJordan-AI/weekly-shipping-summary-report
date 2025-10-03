
# 📈 Weekly Shipping Summary Report (SQLite + Python)
Weekly Shipping Summary Report
> **Portfolio project #2** — Weekly rollups by **Partner + Carrier (+ Factory)** with orders, packages, and shipping totals (fake but realistic data).

---

## Why this matters
Finance/Operations teams often track **weekly** shipping cost trends by **partner** and **carrier** to:
- Reconcile invoices
- Spot cost spikes
- Plan capacity

---

## How to run (in GitHub)

### Option 1 — Codespaces (interactive)
1) Code (green button) → **Create codespace on main**  
2) Terminal:
```bash
pip install -r requirements.txt
python app.py seed
python app.py report --start 2023-12-01 --factory 2 --carrier DHLGM --out weekly_summary.csv
