import json
import os

DATA_FILE = "expenses.json"


class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):
        """Load expenses from a file or return empty list."""
        if not os.path.exists(DATA_FILE):
            return []
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_expenses(self):
        """Save expenses to a JSON file."""
        with open(DATA_FILE, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def add_expense(self):
        """Add a new expense."""
        try:
            name = input("Enter expense name: ").strip()
            amount = float(input("Enter amount: "))
            category = input("Enter category: ").strip()

            entry = {"name": name, "amount": amount, "category": category}
            self.expenses.append(entry)
            self.save_expenses()

            print("\n✔ Expense added successfully!\n")
        except ValueError:
            print("\n Invalid amount. Please enter a number.\n")

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("\nNo expenses recorded yet.\n")
            return

        print("\n--- All Expenses ---")
        for i, exp in enumerate(self.expenses, start=1):
            print(f"{i}. {exp['name']} - ₦{exp['amount']} ({exp['category']})")
        print()

    def view_total(self):
        """Display total spending."""
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"\n Total Spending: ₦{total}\n")

    def search_by_category(self):
        """Search expenses by category."""
        category = input("Enter category to search: ").strip().lower()

        results = [exp for exp in self.expenses if exp["category"].lower() == category]

        if not results:
            print("\nNo expenses found in this category.\n")
            return

        print("\n--- Expenses in Category ---")
        for exp in results:
            print(f"- {exp['name']} - ₦{exp['amount']}")
        print()

    def delete_expense(self):
        """Delete an expense by number."""
        self.view_expenses()
        if not self.expenses:
            return

        try:
            index = int(input("Enter expense number to delete: ")) - 1
            if 0 <= index < len(self.expenses):
                removed = self.expenses.pop(index)
                self.save_expenses()
                print(f"\n✔ Deleted: {removed['name']} (₦{removed['amount']})\n")
            else:
                print("\n Invalid number.\n")
        except ValueError:
            print("\n Please enter a valid number.\n")

    def menu(self):
        """Main program menu."""
        while True:
            print("=== EMEKA’s Expense Tracker ===")
            print("1. Add Expense")
            print("2. View All Expenses")
            print("3. View Total Spending")
            print("4. Search by Category")
            print("5. Delete an Expense")
            print("6. Exit")

            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.view_total()
            elif choice == "4":
                self.search_by_category()
            elif choice == "5":
                self.delete_expense()
            elif choice == "6":
                print("\nGoodbye!\n")
                break
            else:
                print("\n Invalid choice. Try again.\n")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.menu()
