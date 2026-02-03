class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        i = 0 
        if n < 4:
            return False
        while i+1 <n and nums[i] < nums[i+1]:
            i +=1
        p = i
    
        while i+1 <n and nums[i]>nums[i+1]:
            i += 1
        q = i
        con = 1
        for m in range(0,p):
            if nums[m] < nums[m+1]:
                continue
            else:con = 0
        for j in range(p,q):
            if nums[j] > nums[j+1]:
                continue
            else:con = 0
        for k in range(q,n-1):
            if nums[k]<nums[k+1]:
                continue
            else:con = 0
        
        if con == 1:
            return True
        else:
            return False
        
        
my = Solution()
print(my.isTrionic([1,3,5,4,2,6]))