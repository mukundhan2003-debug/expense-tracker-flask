import csv

def view_expenses():
    try:
        with open("expenses.csv", mode='r') as file:
            reader = csv.reader(file)
            print("\n--- All Expenses---")
            for row in reader:
                print(f"Amount: {row[0]}, Category: {row[1]}, Date: {row[2]}")
    except FileNotFoundError:
            print("No expenses found.")

