'''Write a Python program to print all prime numbers between two numbers.'''

start_num = int(input("Enter a starting point : "))
end_num = int(input("Enter a ending point : "))



for num in range(start_num, end_num + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
            
     
    