''' Q)You are given an array A of size N,where each element represents the number of cupcakes sold in a single transaction.
Your task is to find and return an integer value representing the sum of cupcakes from the transactions where 5 or more cupcakes were sold.
Return 0 if there is no transaction with more than 5 cupcakes sold.            '''
    
def cupcakes(n,arr):
    sum=0
    for i in range(n):
        if arr[i]>=5:
            sum+=arr[i]
    return sum      #print(sum)
n=5                 #cupcakes(5,[1,2,5,8,3,7])
arr=[1,2,5,8,3,7]  
print(cupcakes(n,arr))
