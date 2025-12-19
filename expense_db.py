import sqlite3

DB_NAME = "expenses.db"

#This defines the function for connecting the database to the main script
def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cur = conn.cursor()
#This creates the table as long as one doesn't already exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT
        );
    """)

    conn.commit()
    conn.close()

#defines function for adding expenses 
def add_expense(amount, category, date, description):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO expenses (amount, category, date, description)
        VALUES (?, ?, ?, ?);
    """, (amount, category, date, description))

    conn.commit()
    conn.close()

#defines function for listing expenses
def list_expenses():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM expenses;")
    rows = cur.fetchall()

    conn.close()
    return rows

#defines function for updating expenses
def update_expense(expense_id, amount, category, date, description):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, date = ?, description = ?
        WHERE id = ?;
    """, (amount, category, date, description, expense_id))

    conn.commit()
    conn.close()

#defines function for deleting expenses
def delete_expense(expense_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM expenses WHERE id = ?;", (expense_id,))
    conn.commit()
    conn.close()
