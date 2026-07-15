import sqlite3
from pathlib import Path

DB_PATH = Path("data/jobs.db")


def init_database():

    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        title TEXT,

        company TEXT,

        location TEXT,

        remote INTEGER,

        url TEXT UNIQUE,

        description TEXT,

        score INTEGER,

        status TEXT
    )
    """)

    conn.commit()

    conn.close()