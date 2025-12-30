#printing first 4 natural numbers in reverse

def kk(n):
    if n==5:
        return
    kk(n+1)
    print(n)
kk(1)