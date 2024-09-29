import json
from datetime import datetime

# Global variable to store expenses
expenses = []

# Load expenses from a file if it exists
def load_data():
    global expenses
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []

# Save expenses to a file
def save_data():
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

# Function to add a new expense
def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        print("Select a category: 1) Food  2) Transportation  3) Entertainment  4) Other")
        category_choice = int(input("Enter the category number: "))
        category = get_category(category_choice)
        
        if category:
            expense = {
                'amount': amount,
                'description': description,
                'category': category,
                'date': str(datetime.now().date())
            }
            expenses.append(expense)
            save_data()
            print("Expense added successfully!\n")
        else:
            print("Invalid category! Please try again.")
    except ValueError:
        print("Invalid input! Please enter the correct values.")

# Helper function to get the category based on user input
def get_category(choice):
    categories = {
        1: "Food",
        2: "Transportation",
        3: "Entertainment",
        4: "Other"
    }
    return categories.get(choice)

# Function to view summary of all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    
    print("\n--- Expense Summary ---")
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Description: {expense['description']}, "
              f"Category: {expense['category']}, Date: {expense['date']}")
    print()

# Function to view expenses by category
def view_expenses_by_category():
    print("Select a category: 1) Food  2) Transportation  3) Entertainment  4) Other")
    try:
        category_choice = int(input("Enter the category number: "))
        category = get_category(category_choice)
        
        if category:
            filtered_expenses = [expense for expense in expenses if expense['category'] == category]
            if filtered_expenses:
                print(f"\n--- {category} Expenses ---")
                for expense in filtered_expenses:
                    print(f"Amount: {expense['amount']}, Description: {expense['description']}, Date: {expense['date']}")
            else:
                print(f"No expenses found for category: {category}\n")
        else:
            print("Invalid category! Please try again.")
    except ValueError:
        print("Invalid input! Please enter the correct values.")

# Function to display monthly summary
def monthly_summary():
    current_month = datetime.now().month
    current_year = datetime.now().year
    monthly_expenses = [expense for expense in expenses
                        if datetime.strptime(expense['date'], "%Y-%m-%d").month == current_month
                        and datetime.strptime(expense['date'], "%Y-%m-%d").year == current_year]

    if not monthly_expenses:
        print("No expenses recorded for this month.\n")
        return

    total_spent = sum(expense['amount'] for expense in monthly_expenses)
    print(f"\n--- Monthly Summary for {current_month}/{current_year} ---")
    print(f"Total spent: {total_spent}")
    
    categories = ['Food', 'Transportation', 'Entertainment', 'Other']
    for category in categories:
        category_total = sum(expense['amount'] for expense in monthly_expenses if expense['category'] == category)
        print(f"Total spent on {category}: {category_total}")
    print()

# Main menu for the expense tracker
def main_menu():
    load_data()
    while True:
        print("Expense Tracker Menu:")
        print("1) Add a new expense")
        print("2) View all expenses")
        print("3) View expenses by category")
        print("4) View monthly summary")
        print("5) Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                view_expenses_by_category()
            elif choice == 4:
                monthly_summary()
            elif choice == 5:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the application
if __name__ == "__main__":
    main_menu()
