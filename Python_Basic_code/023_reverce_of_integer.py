# Write a Python program to reverse a given integer.


print("Start of program")

input_data = input("Enter a number :")

reversed=''
for x in input_data:
    reversed = x + reversed


print("Reverced string : ",reversed)
print("End of program")

