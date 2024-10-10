print("Start of program")

fact = int(input("Enter a number to find Factorial "))
counter=fact-1
i = 1
findfact=fact
while i < fact:
    findfact=findfact*counter
    counter=counter-1
    i=i+1

print(findfact," is factorial of ",fact)

print("End of program")
