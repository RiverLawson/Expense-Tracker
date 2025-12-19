#this imports the table from the SQLite script
import expense_db as db

#This prints the menu options
def show_menu():
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")

#This is the main loop, all logic happens inside here. 
def main():
    db.init_db()
#If there is a table or a table was created, then prompt the user for input
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        # If user chooses 1, prompt them to add information
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ").strip()
            date = input("Enter date (MM-DD-YYYY): ").strip()
            description = input("Enter description: ").strip()

            db.add_expense(amount, category, date, description)
            print("Expense added.")

        # If user chooses 2, then list expenses
        
        elif choice == "2":
            expenses = db.list_expenses()
            if not expenses:
                print("No expenses found.")
            else:
                for expense in expenses:
                    print(expense)

        # If the user chooses 3, prompt user to input an item ID, then have user update that expense
        elif choice == "3":
            expense_id = int(input("Enter expense ID to update: "))
            amount = float(input("Enter new amount: "))
            category = input("Enter new category: ").strip()
            date = input("Enter new date (MM-DD-YYYY): ").strip()
            description = input("Enter new description: ").strip()

            db.update_expense(expense_id, amount, category, date, description)
            print("Expense updated.")

        # If user chooses 4, prompt user to input an item ID, then delete that expense
        elif choice == "4":
            expense_id = int(input("Enter expense ID to delete: "))
            db.delete_expense(expense_id)
            print("Expense deleted.")

        # If user chooses 5, exit
        elif choice == "5":
            print("Exiting...")
            break
        #if the user doesn't type a valid input, prompt user to try again. 
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
