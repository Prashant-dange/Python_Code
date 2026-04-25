'''Write a Python program to calculate the compound interest.'''

principal_amt = int(input("Enter a principal amount : "))
Rate_of_intrest = float(input("Enter a rate of intrest : "))
Tenure = int(input("Enter a Tenure : "))


CI = principal_amt * (1 + Rate_of_intrest/100) ** Tenure - principal_amt


print("Compound intrest is : ",CI," Total Amount ", (CI+principal_amt))