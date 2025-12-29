class Solution:
    def addDigits(self,num):
        while num>=10:
            sumi=0
            while num>0:
                rem=num%10
                sumi+=rem
                num=num//10
            num=sumi
        return num
s1=Solution()
print(s1.addDigits(34))