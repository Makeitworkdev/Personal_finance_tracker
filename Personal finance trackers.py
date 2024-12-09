#a program that takes in all income, expenses, calculates the expenses against a set budget and savings amount
#figure out how to include tax deductions on the gross income
x= int(input("Enter your total monthly income amount here: ")) #users to input their income amount
print(x)

y = int(input("Enter the amount spent monthly here: "))   #user inputs their expenses amount
print(y)

z=x-y
print(f'Your monthly balance is: ', z)

Finances={
    "Income":x,
    "Expenses":y,
    "Balance":z
}

print(Finances)


    

        
     
 