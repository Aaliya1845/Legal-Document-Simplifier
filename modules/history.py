import sqlite3
import os
from datetime import datetime

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)

DB_PATH = os.path.join("database", "history.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        content TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_history(action, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (action, content, timestamp) VALUES (?, ?, ?)",
        (action, content, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows
