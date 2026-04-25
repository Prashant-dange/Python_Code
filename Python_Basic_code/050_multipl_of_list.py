'''Write a Python program to multiply all elements in a list.'''


input_list=[42, 7, 19, 73, 5, 88, 31, 60, 14, 27]
multiplication=input_list[0]
i=1

while i < len(input_list):
    multiplication=multiplication*input_list[i]
    i=i+1


print("Multiplication of list element : ",multiplication)