"""Database helpers — safe baseline version."""

import sqlite3


def get_user(user_id: int) -> dict | None:
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    return {"id": row[0], "name": row[1]} if row else None
