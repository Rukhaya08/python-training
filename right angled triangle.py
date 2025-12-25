version-1
x=int(input())
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print()

version-2 (using numbers)
x=int(input())
for i in range(x):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

version-3 
x=int(input())
for i in range(1,x+1):
    print("*"*i)

