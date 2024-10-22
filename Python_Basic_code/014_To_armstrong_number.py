print("Start of program")

num=int(input("Enter a number to check Armstrong no : "))

sum=0

temp=num

while temp > 0 :
    digit = temp %10
    sum += digit**3
    temp//=10

if sum==sum:
    print(num," is an armstong number")
else:
    print(num," is not armstrong number")




print("End of program")