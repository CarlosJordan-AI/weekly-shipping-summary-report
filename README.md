
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

<img width="378" height="512" alt="image" src="https://github.com/user-attachments/assets/602f50ad-337a-46df-a46e-38d2840e7a72" />

After it complete running (about 15 seg), enter in the workflow and download the file for preview:

<img width="1545" height="549" alt="image" src="https://github.com/user-attachments/assets/be1c09d7-635b-4d48-b5b0-b72c1435d644" />

Output preview:
<img width="1456" height="650" alt="image" src="https://github.com/user-attachments/assets/e3c9ca46-6101-4ed8-a6b0-34245b5e0dc1" />


