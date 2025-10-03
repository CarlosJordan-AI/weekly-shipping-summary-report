
# 📈 Weekly Shipping Summary Report (SQLite + Python)

> This project showcases how SQL + Python automation can generate reports used in real-world logistics or finance workflows.
> This demo uses **fake but realistic data** to simulate a real-world **operations & finance report**:
> 
Weekly Shipping Summary Report
> — Weekly rollups by **Partner + Carrier + Factory** with orders, packages, and shipping totals (fake but realistic data).


---

### 🔍  Why this matters
Finance/Operations teams often track **weekly** shipping cost trends by **partner** and **carrier** to:
- Reconcile invoices
- Spot cost spikes
- Plan capacity
- Audit invoice payments

---

### ⚙️ How it works
This small pipeline combines:
- 🗃️ **SQLite** (lightweight fake database)
- 💡 **SQL** report (`report.sql`)
- 🐍 **Python CLI** (`app.py`) to:
  - seed fake data  
  - execute the report  
  - export the results as a CSV  
- ⚡ **GitHub Actions workflow** for one-click report generation directly on GitHub 

---

## How to run (in GitHub)

### Option 1 — Codespaces (interactive)
1) Code (green button) → **Create codespace on main**  
2) Terminal:
```bash
pip install -r requirements.txt
python app.py seed
python app.py report --start 2023-12-01 --factory 2 --carrier DHLGM --out weekly_summary.csv
```

---

### Option 2 — Workflows (interactive)
Run the below Workflow:

[![Run Summary](https://github.com/<CarlosJordan-AI>/weekly-shipping-summary-report/actions/workflows/run-summary.yml/badge.svg)](../../actions/workflows/run-summary.yml)

Run the workflow:

<img width="1320" height="546" alt="image" src="https://github.com/user-attachments/assets/707ff919-d4a6-4514-82dc-15dd4f02e6ca" />


After it completes (about 15 seg), enter in the workflow and download the file for preview:

<img width="1532" height="538" alt="image" src="https://github.com/user-attachments/assets/5f987359-ff7f-4931-b131-ca5fd117b5f5" />


Output preview:
<img width="386" height="660" alt="image" src="https://github.com/user-attachments/assets/d0ef4204-a640-4ce8-9c71-b280caf1e34d" />


### 🧠 Key highlights
- Parameterized SQL query (`:partner`, `:factory`, `:start`)  
- Reproducible fake dataset seeded automatically  
- Outputs `shipments.csv` with order, carrier, and invoice data  
- Optional: run interactively in **Codespaces**, or trigger via **GitHub Actions**  
