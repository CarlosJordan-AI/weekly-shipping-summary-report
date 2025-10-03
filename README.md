
# 📈 Weekly Shipping Summary Report (SQLite + Python)
Weekly Shipping Summary Report
> — Weekly rollups by **Partner + Carrier + Factory** with orders, packages, and shipping totals (fake but realistic data).

[![Run Summary](https://github.com/<CarlosJordan-AI>/weekly-shipping-summary-report/actions/workflows/run-summary.yml/badge.svg)](../../actions/workflows/run-summary.yml)
---

## Why this matters
Finance/Operations teams often track **weekly** shipping cost trends by **partner** and **carrier** to:
- Reconcile invoices
- Spot cost spikes
- Plan capacity
- Audit invoice payments

---

## How to run (in GitHub)

### Option 1 — Codespaces (interactive)
1) Code (green button) → **Create codespace on main**  
2) Terminal:
```bash
pip install -r requirements.txt
python app.py seed
python app.py report --start 2023-12-01 --factory 2 --carrier DHLGM --out weekly_summary.csv
