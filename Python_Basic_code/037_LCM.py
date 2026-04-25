a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find HCF using Euclidean algorithm
x, y = a, b
while y != 0:
    x, y = y, x % y
hcf = x

# Find LCM using the relation
lcm = (a * b) // hcf

print("LCM is:", lcm)