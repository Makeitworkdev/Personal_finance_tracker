import matplotlib.pyplot as plt 
import datetime
import calendar 


# Get current date, month and year
current_date = datetime.datetime.now()
current_month = current_date.month   
current_year = current_date.year
current_month_name = current_date.strftime('%B')  # Get the name of the current month

# Get number of days in the current month
days_in_month = calendar.monthrange(current_year, current_month)

def process_date(day=None, month=None, year=None):
    if day is None or month is None or year is None:
        # Use current date if any of the day, month, or year is not provided
        current_date = datetime.datetime.now()
        day = current_date.day if day is None else day
        month = current_date.month if month is None else month
        year = current_date.year if year is None else year     

    # Process the date
    print(f"Processing date: {day}-{month}-{year}")
    return month, year


def get_input(prompt, input_type=float):
    """
    Helper function to handle user input with input type validation.
    """
    while True:
        try:
            return input_type(input(prompt))  # Convert input to the specified type
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
def get_expenses(expense_type):
    #function to get expenses from the user.

    expenses = {}
    
    while True:
        # Ask the user if they want to add an expense
        add_expense = input(f"Do you want to add an {expense_type} expense? (yes/no): ").strip().lower()
        
        if add_expense == "no":
            break
        elif add_expense == "quit":
            print("Exiting expense input.")
            break
        elif add_expense == "yes":
            expense_name = input("Enter the name of the expense: ")
            expense_amount = get_input("Enter the amount of the expense: ", float)
            expense_frequency = ""
            
            if expense_type == "recurring":
                expense_frequency = input("How often does this expense occur? (daily/monthly/weekly/fortnightly(once every 2 weeks)/weekdays/weekends): ").strip().lower()
                #calculate monthly expense from recurring expenses
                if expense_frequency == "daily":
                    expense_amount *= days_in_month
                elif expense_frequency == "fortnightly":
                    expense_amount *= 2 
                elif expense_frequency == "weekly":
                    expense_amount *= 4 
                elif expense_frequency == "weekdays":
                    expense_amount *= 5 * 4  #assumed Monday- Friday
                elif expense_frequency == "weekends":
                    expense_amount *= 2 * 4  #assumed saturday and sunday weekends
                elif expense_frequency == "monthly":
                    expense_amount = expense_amount
                

            # Store expense details in a dictionary
            expenses[expense_name] = {
                "amount": expense_amount,
                "frequency": expense_frequency
            }
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")
    
    return expenses

def get_categories(expenses):
    """function to get the expenses into categories.
    The catergories include rent, groceries, transport, water, electricity, entertainment, restaurants/leisure, miscellaneous."""
    categories = {}
    for expense_name, expense in expenses.items():  # expense_name is the key
        category = input(f"Enter the category for expense '{expense_name}' (e.g., rent, subscription, food, etc.): ")
        if category not in categories:
            categories[category] =  0
        categories[category] += expense['amount']
    return categories
        
def plot_expenses(expenses):
    #plots expenses
    category = list(expenses.keys())
    amounts = list(expenses.values())
    month, year = process_date(month = current_month, year = current_year)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.xlabel('Categories')
    plt.ylabel('Amount (Ksh)')
    plt.title(f'Expenditure breakdown for {calendar.month_name[month]} {year}')
    plt.bar(category, amounts)
    plt.show()



def main():
    print("Welcome to the Financial Tracker System!")
    print(" ")

    # Collecting user inputs
    income = get_input("Enter your total income (in Ksh): ", float)
    initial_expenses = get_expenses("initial")
    recurring_expenses = get_expenses("recurring")
    budget = get_input("Enter your budget (in Ksh): ", float)
    savings = get_input("Enter your current savings (in Ksh): ", float)
   
    #combine total expenses
    total_initial_expenses = sum(expenses.get("amount") for expenses in initial_expenses.values())
    total_recurring_expenses = sum(expenses.get("amount") for expenses in recurring_expenses.values())
    total_expenses = total_initial_expenses + total_recurring_expenses

    # Simple financial computations
    balance = income - total_expenses
    remaining_budget = budget - total_expenses
    total_savings = savings + balance

    #categorize expenses
    categorized_expenses = get_categories(initial_expenses)
    categorized_expenses.update(get_categories(recurring_expenses))

    #plot expenses
    plot_expenses(categorized_expenses)

    
    # Displaying results
    month, year = process_date(month=current_month, year = current_year)
    print("\n--- Financial Summary ---")
    print(f"Total Monthly Income: Ksh{income:.2f}")
    print(f"Total Monthly Expenses: Ksh{total_expenses:.2f}")
    print(f"Remaining Balance: Ksh{balance:.2f}")
    print(f"Remaining Budget: Ksh{remaining_budget:.2f}")
    print(f"Total Savings (including balance) for the month of {calendar.month_name[month]} {year}: Ksh{total_savings:.2f}")

if __name__ == "__main__":
    main()
    
