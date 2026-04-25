'''Write a Python program to calculate the simple interest.'''

principal_amt = int(input("Enter a principal amount : "))
Rate_of_intrest = float(input("Enter a rate of intrest : "))
Tenure = int(input("Enter a Tenure : "))

simple_intrest = (principal_amt * Rate_of_intrest * Tenure)/100


comulative_amt = simple_intrest + principal_amt

print("Principal : ",principal_amt, " intrest : ",simple_intrest, " Total : ",comulative_amt)

