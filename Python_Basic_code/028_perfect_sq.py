'''Write a Python program to check if a number is a perfect square.'''


num = int(input("Enter a number: "))

sqrt_num = num ** 0.5  # square root


if sqrt_num == int(sqrt_num):
    print(f"{num} is a perfect square.")
else:
    print(f"{num} is not a perfect square.")