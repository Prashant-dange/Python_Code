'''Write a Python program to check if an element exists in a list.'''

print("Start of the program")

storage_list = [10,20,30,50,1,3,5,6,8,12]


input_num = int(input("Enter a number to check in list : "))

i=0

while i < len(storage_list):
    check =0
    if input_num == storage_list[i]:
        print(input_num," is present in list ")
        check=1
        break
    i=i+1


if check == 0:
    print(input_num," is not present in list ")

