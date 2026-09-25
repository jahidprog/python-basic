import json
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    title = input("Expense title: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['title']} | "
            f"{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['date']}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\n💰 Total spending: {total:.2f}")


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n--- Category Summary ---")

    for category, amount in summary.items():
        print(f"{category}: {amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()