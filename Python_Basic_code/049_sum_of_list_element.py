'''Write a Python program to find the sum of elements in a list.'''


input_list= [42, 7, 19, 73, 5, 88, 31, 60, 14, 27]

sum=0
i=0
while i < len(input_list):
    sum=sum+input_list[i]
    i=i+1


print("Sum of List element : ",sum)

