'''Write a Python program to check if a year is a leap year or not.'''


input_year = int(input("Enter a year to cehck Leap year : "))

if (input_year % 4 == 0 and input_year % 100 != 0 )or ( input_year % 400 ==0 ):
    print(input_year,"is leap year")
else:
    print(input_year,"is not leap year")