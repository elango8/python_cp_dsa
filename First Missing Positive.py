class Solution:
    def firstMissingPositive(self, nums):
        missing = 1
        for i in range(1,len(nums)+1):
            if i in nums:
                continue
            else:
                missing = i
                break 
        return missing
    
my = Solution()
print(my.firstMissingPositive([1,2,0]))