import matplotlib.pyplot as plt 
import datetime
import calendar 

#get current date, month and year 
current_date = datetime.datetime.now() 
current_month = current_date.month   
current_year = current_date.year
current_month_name = current_date.strftime('%B') #get the name of the current month

#get number of days in the current month
days_in_month = calendar.monthrange(current_year, current_month)

def get_input(prompt, input_type=float):
    """
    Helper function to handle user input with input type validation.
    """
    while True:
        try:
            return input_type(input(prompt))  # Convert input to the specified type
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
def get_recurring_expenses():
    """
    Function to get recurring expenses from the user.
    """
    recurring_expenses = []
    
    while True:
        # Ask the user if they want to add a recurring expense
        add_expense = input("Do you want to add a recurring expense? (yes/no): ").strip().lower()
        
        if add_expense == "no":
            break
        elif add_expense == "yes":
            expense_name = input("Enter the name of the expense (e.g., rent, subscription): ")
            expense_amount = get_input("Enter the amount of the expense: ", float)
            expense_frequency = input("How often does this expense occur? (daily/monthly/weekly/weekdays/weekends): ").strip().lower()

            
            #calculate monthly expense from recurring expenses
            if expense_frequency == "daily":
                expense_amount = expense_amount*days_in_month
            elif expense_frequency == "weekly":
                expense_amount = expense_amount*4 
            elif expense_frequency == "weekdays":
                expense_amount = expense_amount*5*4  #assumed Monday- Friday
            elif expense_frequency == "weekends":
                expense_amount = expense_amount*2*4  #assumed saturday and sunday weekends


            
            # Store expense details in a dictionary
            recurring_expenses.append({
                "name": expense_name,
                "amount": expense_amount,
                "frequency": expense_frequency
            })
        else:
            print("Invalid response. Please answer 'yes' or 'no'.")
    
    return recurring_expenses

def main():
    print("Welcome to the Financial Tracker System!")

    # Collecting user inputs
    income = get_input("Enter your total income: Ksh", float)
    expenses = get_input("Enter your total expenses: Ksh", float)
    budget = get_input("Enter your budget: Ksh", float)
    savings = get_input("Enter your current savings: Ksh", float)

    #get recurring expenses
    recurring_expenses = get_recurring_expenses()

    #calculate total recurring expenses
    total_recurring_expenses = sum(expense["amount"] for expense in recurring_expenses)

    #combine total expenses
    total_expenses = expenses + total_recurring_expenses

    # Simple financial computations
    balance = income - total_expenses
    remaining_budget = budget - total_expenses
    total_savings = savings + balance

    # Displaying results
    print("\n--- Financial Summary ---")
    print(f"Total Monthly Income: Ksh{income:.2f}")
    print(f"Total Monthly Expenses: Ksh{total_expenses:.2f}")
    print(f"Remaining Balance: Ksh{balance:.2f}")
    print(f"Remaining Budget: Ksh{remaining_budget:.2f}")
    print(f"Total Savings (including balance) for the month of {current_month_name}: Ksh{total_savings:.2f}")

if __name__ == "__main__":
    main()
    
