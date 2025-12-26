def cupcakes(n,arr):
    sum=0
    for i in range(n):
        if arr[i]>=5:
            sum+=arr[i]
    return sum      #print(sum)
n=5                 #cupcakes(5,[1,2,5,8,3,7])
arr=[1,2,5,8,3,7]  
print(cupcakes(n,arr))