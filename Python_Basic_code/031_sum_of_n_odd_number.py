'''Write a Python program to find the sum of odd numbers up to n.'''


n_number = int(input("Enter a n number : "))

sum=0
i=0

while i <= n_number:
    if i%2!=0:
        sum=sum+i
    i=i+1



print("Sum of n th number is ",sum)