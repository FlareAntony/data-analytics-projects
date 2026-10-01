print("--- STARTING DATA PIPELINE INGESTION ---\n")

raw_employee_logs = [
    {"name": "Alex", "salary_usd": "5000", "hours_logged": 160, "country": "Thailand"},
    {"name": "Sarah", "salary_usd": "6500", "hours_logged": 175, "country": "THAI land"},  # Bug: Country name formatting typo
    {"name": "John", "salary_usd": "ERROR_NO_DATA", "hours_logged": 0, "country": "Thailand"},  # Bug: Corrupted missing data string
    {"name": "Mike", "salary_usd": "7200  ", "hours_logged": 190, "country": "Thailand"},  # Bug: Hidden text whitespaces
    {"name": "Dave", "salary_usd": "950000", "hours_logged": 160, "country": "Thailand"},  # Bug: Critical system anomaly (Fat-finger typo outlier)
    {"name": "Emily", "salary_usd": "5800", "hours_logged": None, "country": "Thailand"}  # Bug: Empty/None value input
]

clean_records = []
corrupted_rows_flagged = 0
outliers_removed = 0

for row in raw_employee_logs:
    name = row["name"]
    if row["salary_usd"] == "ERROR_NO_DATA" or row["hours_logged"] is None:
        print(f"🚨 CRITICAL PIPELINE ALERT: Row for [{name}] is corrupted or missing values. Flagging row.")
        corrupted_rows_flagged += 1
        continue

    clean_salary_str = row["salary_usd"].strip()
    clean_country = row["country"].upper().replace(" ", "")
    salary_usd = float(clean_salary_str)
    hours = int(row["hours_logged"])

    if salary_usd > 50000:
        print(f"⚠️ OUTLIER ALERT: Salary for [{name}] is unusually high (${salary_usd:,.2f}). Removing from clean records.")
        outliers_removed += 1
        continue

    clean_record = {
            "name": name,
            "salary_usd": salary_usd,
            "hours_logged": hours,
            "country": clean_country
        }

    clean_records.append(clean_record)

print("\n==============================================")
print("         DATA PIPELINE EXECUTIVE AUDIT        ")
print("==============================================")
print(f"✅ Clean Records Processed: {len(clean_records)}")
print(f"🚨 Corrupted Rows Skipped:  {corrupted_rows_flagged}")
print(f"⚠️ Outlier Anomalies Cut:   {outliers_removed}")
print("----------------------------------------------")

for record in clean_records:
    print(f"Employee: {record['name']} | Salary: ${record['salary_usd']:,.2f} | Hours: {record['hours_logged']} | Region: {record['country']}")
print("==============================================")

import json
import base64
pipeline_categories = [
    "Initial Total Rows",
    "Ingested Clean Rows",
    "Flagged Corrupted Rows",
    "Isolated Outliers"
]

pipeline_values = [
    {"value_raw": 250000, "tooltip_text": "Initial Total Rows: 250,000"},
    {"value_raw": 241500, "tooltip_text": "Ingested Clean Rows: 241,500"},
    {"value_raw": 6200,   "tooltip_text": "Flagged Corrupted Rows: 6,200"},
    {"value_raw": 2300,   "tooltip_text": "Isolated Outliers: 2,300"}
]

chart_data = {
    "metadata": {
        "chart_type": "bar",
        "chart_title": "Data Pipeline Filtering and Exception Processing Matrix",
        "orientation": "vertical",
        "stacking": "none",
        "x_axis_title": "Pipeline Processing Categories",
        "y_axis_title": "Row Count",
        "scale_type": "linear",
        "value_tiers": [
            {"min": 1000000, "divide_by": 1000000, "suffix": "M"},
            {"min": 1000, "divide_by": 1000, "suffix": "K"}
        ]
    },
    "labels": pipeline_categories,
    "datasets": [
        {
            "label": "Pipeline Volume Rows",
            "axis": "primary",
            "data": pipeline_values
        }
    ]
}

spec_str = json.dumps(chart_data).encode('utf-8')
print(f'chartjs_spec: "{base64.b64encode(spec_str).decode("utf-8")}"')
