'''Write a Python program to find the length of a list.'''

print("Start of the program")

input_list = input("Enter list space or comma seprated : ")

cleaned_list = []

i=0
while i < len(input_list):
    if input_list[i] != ',' and input_list[i] != ' ':
        cleaned_list.append(input_list[i])
    
    i=i+1


j=0
while j < len(cleaned_list):
    j=j+1


print("Lenght of list is ",j)
