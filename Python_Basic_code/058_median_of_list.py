'''Write a Python program to find the median of a list.'''

input_list= input("Enter a list to find meadian : ")

cln_list = input_list.split()

for i in range(0,len(input_list)):
    cln_list[i]= int(input_list[i])

print(cln_list)