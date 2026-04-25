'''Write a Python program to sort a list in ascending order.'''

input_list=[45, 12, 78, 34, 23, 89, 67, 10]

print("Before sort",input_list)

i=0
while i < len(input_list):
    j=0
    while j < len(input_list)-i-1:
        if input_list[i] < input_list[j]:
            temp=input_list[j]
            input_list[j]=input_list[i]
            input_list[i]=temp
        j=j+1
    i=i+1


print("After sort",input_list)