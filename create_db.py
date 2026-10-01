import sqlite3

conn = sqlite3.connect("company_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS payroll_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    salary_usd TEXT,
    hours_logged INTEGER,
    country TEXT
)
""")

dirty_rows = [
    ("Alex", "5000", 160, "Thailand"),
    ("Sarah", "6500", 175, "THAI land"),
    ("John", "ERROR_NO_DATA", 0, "Thailand"),
    ("Mike", "7200  ", 190, "Thailand"),
    ("Dave", "950000", 160, "Thailand"),
    ("Emily", "5800", None, "Thailand")
]

cursor.executemany("INSERT INTO payroll_logs (name, salary_usd, hours_logged, country) VALUES (?, ?, ?, ?)", dirty_rows)
conn.commit()
conn.close()
print("🎉 Success! 'company_data.db' has been created and loaded with dirty data.")
