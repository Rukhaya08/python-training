def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]
nums=list(map(int,input().split()))
print(majorityElement(nums))