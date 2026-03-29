import csv

def show_summary():
    total = 0

    try:
        with open("expenses.csv", mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[0])

        print("\n Total Expense: ", total)

    except FileNotFoundError:
        print("No data found.")