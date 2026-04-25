'''Write a Python program to find the HCF of two numbers.'''

'''Using Division (Euclidean) Method'''



a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclidean algorithm
while b != 0:
    a, b = b, a % b

print("HCF is:", a)

