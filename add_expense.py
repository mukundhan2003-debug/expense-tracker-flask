import csv

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    with open("expense.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, date])

    print("Expense added successfully!")