import sqlite3

DATABASE_NAME = "library.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS students(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        student_id TEXT UNIQUE,

        full_name TEXT NOT NULL,

        father_name TEXT NOT NULL,

        mother_name TEXT NOT NULL,

        mobile TEXT NOT NULL,

        whatsapp TEXT NOT NULL,

        dob TEXT NOT NULL,

        gender TEXT NOT NULL,

        address TEXT NOT NULL,

        preparing_for TEXT NOT NULL,

        seat_number TEXT,

        seat_mode TEXT,

        monthly_fee REAL,

        fee_status TEXT DEFAULT 'Pending',

        status TEXT DEFAULT 'Active',

        photo TEXT NOT NULL,

        aadhaar_photo TEXT NOT NULL,

        joining_date TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    conn.commit()

    conn.close()