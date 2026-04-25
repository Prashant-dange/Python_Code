'''Write a Python program to check if a character is a vowel or consonant.'''

str_input = input("Enter a char to check it vowels or consonant : ")

str_input = str_input.lower()
vowels = ['a','e','i','o','u']

cnt=0

check=0
while check < len(vowels):
    if str_input == vowels[check]:
        cnt=cnt+1
    check=check+1

if cnt > 0 :
    print("it is vowels")
else:
    print("it is consonant")

    
