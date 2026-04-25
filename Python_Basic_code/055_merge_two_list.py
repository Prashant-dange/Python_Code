'''Write a Python program to merge two lists into one.'''

list1 = [45, 12, 78, 34, 23, 89, 67, 10]
list2 = [5, 99, 32, 18, 76, 41, 63, 27]



i=0
while i < len(list2):
    list1.append(list2[i])
    i=i+1


print("after merging",list1)