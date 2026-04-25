# Write a Python program to calculate the sum of squares of first n natural numbers.

n_num = int(input("Enter a n natural number for sum of Sq : "))

i=1
sum=0

while i <= n_num :
    sq = i * i
    sum = sum + sq
    i = i+1


print("sum of sq is ", sum)


