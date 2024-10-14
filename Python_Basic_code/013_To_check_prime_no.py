print("Start of program")
import sys
num=int(input("Enter number to check prime or not : "))

i=2
test=0
while i < num:
    if (num%i==0):
        print(num,"is Not Prime")
        test=1
        sys.exit(0)
    i=i+1

if test ==0:
    print("is prime")

print("End of program")