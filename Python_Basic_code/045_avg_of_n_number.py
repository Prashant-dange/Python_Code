# Write a Python program to find the average of n numbers.

n_num = int(input("Enter a number : "))

i=0
sum=0
while i <= n_num:
    sum=sum+i
    i=i+1


avg=sum/(i-1)

print("Avg of n number is ",avg)