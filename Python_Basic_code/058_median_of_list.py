'''Write a Python program to find the median of a list.'''

input_list= input("Enter a list to find meadian : ")

new_list = input_list.split()

i=0
while i < len(new_list):
    new_list[i]=int(new_list[i])
    i=i+1

cln_list=sorted(new_list)

print(cln_list, "and length is ",len(cln_list))

length = len(cln_list)
if length % 2 == 0:
    evenindex=int(length/2)
    print(evenindex)
    meadian=(cln_list[evenindex] + cln_list[evenindex-1])/2
    print("Median is ",meadian)
else:
    index=int(length/2)
    print("Meadian is ",cln_list[index])

