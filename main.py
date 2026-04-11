from tkinter import *
import sqlite3
import matplotlib.pyplot as plt

# ---------- DATABASE ----------
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    type TEXT
)
""")

conn.commit()
conn.close()

# ---------- UI ----------
root = Tk()
root.title("Expense Tracker")
root.geometry("500x500")

Label(root, text="Expense Tracker", font=("Arial", 16)).pack(pady=10)

Label(root, text="Amount").pack()
amount_entry = Entry(root)
amount_entry.pack()

Label(root, text="Category").pack()
category_entry = Entry(root)
category_entry.pack()

Label(root, text="Type (Income/Expense)").pack()
type_entry = Entry(root)
type_entry.pack()

# ---------- FUNCTIONS ----------

def add_record():
    amount = amount_entry.get()
    category = category_entry.get()
    type_ = type_entry.get()

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (amount, category, type) VALUES (?, ?, ?)",
                   (amount, category, type_))

    conn.commit()
    conn.close()

    print("Record Added")


def view_records():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def show_chart():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT type, SUM(amount) FROM expenses GROUP BY type")
    data = cursor.fetchall()

    types = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.bar(types, amounts)
    plt.title("Income vs Expense")
    plt.xlabel("Type")
    plt.ylabel("Amount")

    plt.show()

    conn.close()

# ---------- BUTTONS (OUTSIDE FUNCTIONS) ----------

Button(root, text="Add Record", command=add_record).pack(pady=10)
Button(root, text="View Records", command=view_records).pack()
Button(root, text="Show Chart", command=show_chart).pack(pady=10)

# ---------- RUN ----------
root.mainloop()