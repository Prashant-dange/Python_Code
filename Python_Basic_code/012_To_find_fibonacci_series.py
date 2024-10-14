print("start of program")

L=[0,1]

i=0
while i < 10:
    L.append(L[i]+L[-1])
    i=i+1

print(L)
print("End of program")