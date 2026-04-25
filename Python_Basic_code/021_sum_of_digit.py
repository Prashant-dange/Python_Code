#Write a Python program to find the sum of digits of a number.

print("Start of the program")

input_digit = int(input("Enter a number"))

i=0
sum_of_digit =0
while input_digit > 0 :
    digit = input_digit % 10
    sum_of_digit = sum_of_digit + digit
    input_digit = input_digit // 10


print("sun of digit is ",sum_of_digit)