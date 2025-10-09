import csv
from datetime import datetime

def add_expense():
    try:
        amount = float(input("Enter the amount of the expense: "))
    except ValueError:
        print("Please enter a valid number.")
        amount = float(input("Enter the amount of the expense: "))

    category = input("Enter category (e.g. food, transport, shopping): ")

    date_format = "%Y-%m-%d"
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, date_format)
            break
        except ValueError:
            print("Please enter a valid date.")


    description = input("Enter description: ")

    expenses = {
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    }

    print("Expense added successfully!")
    return expenses

def summary(expenses):
    print("Expenses summary: ")

    total = sum(exp["amount"] for exp in expenses)
    print(f"Total spent: {total:.2f}\n")

    print("By category: ")
    total_category = {}
    for exp in expenses:
        category = exp["category"]
        total_category[category] = total_category.get(category, 0) + exp["amount"]

    for category, amount in total_category.items():
        print(f"{category}: {amount:.2f}\n")

    print("By date: ")
    total_date = {}
    for exp in expenses:
        date = exp["date"]
        total_date[date] = total_date.get(date, 0) + exp["amount"]

    for date, amount in total_date.items():
        print(f"{date}: {amount:.2f}\n")

def export_to_csv(expenses, filename = "expenses.csv"):
    if not expenses:
        print("No expenses found!")
        return

    with open(filename, "w", newline="") as file:
        fieldnames = expenses[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)
        print(f"Expenses exported successfully to {filename}!")



print("Welcome  to Exense Tracker! \nChoose an option: \n1. Add expense\n2. Show summary\n3. Export to CSV\n4. Exit")
expenses = []
while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number!")
        continue
    if choice == 1:
        expenses.append(add_expense())
    elif choice == 2:
        summary(expenses)
    elif choice == 3:
        export_to_csv(expenses, "expenses.csv")
    elif choice == 4:
        print("Thank you for using Exense Tracker!")
        break
    else:
        print("Invalid choice!")


