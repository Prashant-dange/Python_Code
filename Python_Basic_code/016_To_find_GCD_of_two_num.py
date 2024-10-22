print("Start of program")

num1 = int(input("Enter a first number : "))
num2 = int(input("Enter a second number : "))

GCD1=[]
GCD2=[]

i=1
while i <= num1:
    if num1 % i == 0:
        GCD1.append(i)
    i=i+1

i=1
while i <= num2:
    if num2 % i == 0:
        GCD2.append(i)
    i=i+1

GCD3=[]
print(GCD1)
print(GCD2)

i=0
while i < len(GCD1):
    j=0
    while j < len(GCD2):
        if GCD1[i]==GCD2[j]:
            GCD3.append(GCD1[i])
        j=j+1
    i=i+1

print(GCD3)
print(GCD3[-1]," is GCD of two number")
print("End of program")