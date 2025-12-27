#reverse the array
x=[1,2,3,4,5]
l=0
r=len(x)-1
while l<r:
    x[l],x[r]=x[r],x[l]
    l+=1
    r-=1
print(x)

#leetcode moveZeros-283(not used in leetcode)
def moveZeros(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]!=0:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=x+y
    print(z)
nums=[0,1,0,3,12]
moveZeros(nums)
