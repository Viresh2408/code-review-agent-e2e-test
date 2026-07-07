"""Database helpers — SECURED version."""

import sqlite3
import subprocess


# FIXED: Use parameterized query
def search_users(username: str) -> list[dict]:
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users WHERE name = ?", (username,))
    return [{"id": r[0], "name": r[1]} for r in cursor.fetchall()]


# FIXED: Pass arguments as a list and disable shell execution (shell=False)
def run_report(report_name: str) -> str:
    if not report_name.isalnum():
        raise ValueError("Invalid report name")
    result = subprocess.run(
        ["generate_report.sh", report_name],
        shell=False,
        capture_output=True,
        text=True,
    )
    return result.stdout
