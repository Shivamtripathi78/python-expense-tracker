import json
import os
from datetime import date

DATA_FILE = "expenses.json"


def load_expenses():
    """Load saved expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved expenses.")
        return []


def save_expenses(expenses):
    """Save expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Add a new expense."""
    try:
        amount = float(input("Enter amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "amount": round(amount, 2),
        "category": category.title(),
        "description": description or "No description",
        "date": date.today().isoformat()
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")


def view_expenses(expenses):
    """Display all recorded expenses."""
    if not expenses:
        print("\nNo expenses recorded yet.")
        return

    print("\n" + "=" * 75)
    print(f"{'DATE':<14}{'CATEGORY':<18}{'AMOUNT (₹)':<16}{'DESCRIPTION'}")
    print("=" * 75)

    for expense in expenses:
        print(
            f"{expense['date']:<14}"
            f"{expense['category']:<18}"
            f"{expense['amount']:<16.2f}"
            f"{expense['description']}"
        )

    print("=" * 75)


def show_total(expenses):
    """Calculate and display total spending."""
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal spending: ₹{total:.2f}")


def category_summary(expenses):
    """Display spending grouped by category."""
    if not expenses:
        print("\nNo expenses available for summary.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\n--- Spending by Category ---")

    for category, amount in sorted(totals.items()):
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n====== PYTHON EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total Spending")
        print("4. Spending by Category")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            print("Your expenses are saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()