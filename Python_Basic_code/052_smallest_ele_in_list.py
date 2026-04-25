'''Write a Python program to find the smallest element in a list.'''


input_list=input("Enter a list seprated by space or , : ")

cleaned_list=[]

i=0
while i < len(input_list):
    if input_list[i] != ' ' and input_list[i] != ',' :
        temp=int(input_list[i])
        cleaned_list.append(temp)
    i=i+1

print(cleaned_list)

small_ele=0

i=0
while i < len(cleaned_list):
    if cleaned_list[i] < small_ele:
        small_ele=cleaned_list[i]
    i=i+1


print("Smallest element in list",small_ele)