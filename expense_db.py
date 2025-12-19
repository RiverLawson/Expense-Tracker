# expense_db.py
import sqlite3

DB_NAME = "expenses.db"


def get_connection():
    #returns a connection to the SQLite database
    return sqlite3.connect(DB_NAME)

  #This creates the expenses table if it doesn't exist
def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            need_type TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

#This inserts a new expense row into the expenses table
def add_expense(amount, category, date, description, need_type):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO expenses (amount, category, date, description)
        VALUES (?, ?, ?, ?, ?);
    """, (amount, category, date, description, need_type))
    conn.commit()
    conn.close()

#This retrieves all expense rows from the expenses table
def list_expenses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses;")
    rows = cur.fetchall()
    conn.close()
    return rows

#updates an existing expense row by its ID
def update_expense(expense_id, amount, category, date, description, need_type):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, date = ?, description = ?
        WHERE id = ?;
    """, (amount, category, date, description, expense_id))
    conn.commit()
    conn.close()

#deletes an expense row by its ID
def delete_expense(expense_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM expenses WHERE id = ?;", (expense_id,))
    conn.commit()
    conn.close()
