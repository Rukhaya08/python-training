def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]
nums=list(map(int,input().split()))
print(majorityElement(nums))

#without builtin function sort
def majorityElement(nums):
        count=0
        candidate=0
        for num in nums:
            if count==0:
                candidate=num
                count+=1
            elif candidate==num:
                count+=1
            else:
                count-=1
        return candidate
nums=list(map(int,input().split()))
print(majorityElement(nums))
