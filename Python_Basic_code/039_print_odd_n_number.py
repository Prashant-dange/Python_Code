'''Write a Python program to find the sum of even numbers up to n.'''


n_number = int(input("Enter a n number : "))

i=0

while i <= n_number:
    if i%2!=0:
        print(i)
    i=i+1

