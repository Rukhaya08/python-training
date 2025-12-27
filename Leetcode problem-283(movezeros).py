#Leetcode version
def moveZeroes(nums):
        idx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[idx]=nums[i]
                idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0
        return nums

print(moveZeroes([0,1,0,3,12]))


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
