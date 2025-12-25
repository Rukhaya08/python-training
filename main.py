x=int(input())
for i in range(1,x+1):
    if i%15==0:  #multiples of 3 and 5 can be written as multiples of 15
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)

