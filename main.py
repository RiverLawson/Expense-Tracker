import expense_db as db


def show_menu():
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")


def main():
    db.init_db()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        # ADD EXPENSE
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ").strip()
            date = input("Enter date (MM-DD-YYYY): ").strip()
            description = input("Enter description: ").strip()

            db.add_expense(amount, category, date, description)
            print("Expense added.")

        # LIST EXPENSES
        elif choice == "2":
            expenses = db.list_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                for expense in expenses:
                    print(expense)

        # UPDATE EXPENSE
        elif choice == "3":
            expense_id = int(input("Enter expense ID to update: "))
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ").strip()
            date = input("Enter new date (MM-DD-YYYY): ").strip()
            description = input("Enter new description: ").strip()

            db.update_expense(expense_id, amount, category, date, description)
            print("Expense updated.")

        # DELETE EXPENSE
        elif choice == "4":
            expense_id = int(input("Enter expense ID to delete: "))
            db.delete_expense(expense_id)
            print("Expense deleted.")

        # EXIT
        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
