print("start of the program")

num1 = int(input("Enter a first number"))
num2 = int(input("Enter a second number"))
num3 = int(input("Enter a third number"))

if num1 > num2 and num1 > num3:
    print(num1," is Largest number")
elif num2 > num1 and num2 > num3:
    print(num2," is Largest number")
else:
    print(num3," is Largest number")

print("End of program")