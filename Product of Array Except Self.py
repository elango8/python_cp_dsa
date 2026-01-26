class Solution:
    def productExceptSelf(self, nums):
        res = [1]*len(nums)
        pre = pos = 1
        for i in range(len(nums)):
            res[i] = pre
            pre = nums[i] * pre
        for j in range(len(nums)-1,-1,-1):
            res[j] = res[j] * pos
            pos = pos * nums[j]
        return res
        
my = Solution()
print(my.productExceptSelf([1,2,3,4]))