'''Write a Python program to find the second largest number in a list.'''


input_list = input("Enter a list of element space seprated : ")

cleaned_list=input_list.split(" ")

input_list=[]

i=0
while i < len(cleaned_list):
    input_list.append(int(cleaned_list[i]))
    i=i+1

print(input_list)

i=0
while i < len(input_list):
    j=0
    while j < len(input_list)-i-1:
        if input_list[j] < input_list[i]:
            temp=input_list[j]
            input_list[j]=input_list[j+1]
            input_list[j+1]=temp
        j=j+1
    i=i+1


print(input_list)
print("Second largets no is ",input_list[1])
