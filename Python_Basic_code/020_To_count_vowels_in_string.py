# Write a Python program to count the number of vowels in a string.

input_str = input("Enter a string : ")
src_str = input_str.lower()
vowesl = ["a","e","i","o","u"]

i=0
count = 0
while i < len(src_str):
    j=0
    while j < len(vowesl):
        if src_str[i] == vowesl[j]:
            count = count + 1
        j = j +1
    i=i+1

print(count ," vowesl are present")


