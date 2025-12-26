using for:
for r in range(4):
    for c in range(5):
        print("r=",r,"c=",c)
    print()

using while:
r=0
while r<4:
    c=0
    while c<5:
        print(r,c)
        c+=1
    print()
    r+=1
