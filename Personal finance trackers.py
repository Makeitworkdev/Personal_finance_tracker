#a program that takes in all income, expenses, calculates the expenses against a set budget and savings amount
#figure out how to include tax deductions on the gross income
def get_input(prompt, input_type=float):
    """
    Helper function to handle user input with type validation.
    """
    while True:
        try:
            return input_type(input(prompt))  # Convert input to the specified type
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")
def recurring_expenses():
    #function to get recurring expenses from user
    recurring_expenses = []
    while True:
    #ask user if they want to add a recurring expense
    add_expenses = input("Do you want to add a recurring expense? (yes/no): ").strip().lower()   
        if add_expense == "no":
            break
        elif add_expense == "yes":
            expense_name = input("Enter the name of the expense (e.g. rent, subscription): ")
            expense_amount = get_input("Enter amount: ", float)
            expense_frequency = input("Enter the frequency with which this expense is made: (monthly/weekly/yearly)").strip().lower()

        # Store expense details in a dictionary
            recurring_expenses.append({
                "name": expense_name,
                "amount": expense_amount,
                "frequency": expense_frequency
            })
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")
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
    balance = income - expenses
    remaining_budget = budget - expenses
    total_savings = savings + balance

    #Store financial info in a dictionary
    Finances={
    "Total Income": income,
    "Total Expenses": total_expenses,
    "Remaining Balance": balance,
    "Remaining budget": remaining_budget,
    "Total Savings": total_savings
    }

    # Displaying results
    print("\n--- Financial Summary ---")
    print(f"Total Income: Ksh{income:.2f}")
    print(f"Total Expenses: Ksh{total_expenses:.2f}")
    print(f"Remaining Balance: Ksh{balance:.2f}")
    print(f"Remaining Budget: Ksh{remaining_budget:.2f}")
    print(f"Total Savings (including balance): Ksh{total_savings:.2f}")

if __name__ == "__main__":
    main()
    



    

        
     
 
