from add_expense import add_expense
from view_expenses import view_expenses
from summary import show_summary

def menu():
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_summary()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")



