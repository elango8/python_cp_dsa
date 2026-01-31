class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        if 1 not in nums:
            return 1

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

            
my = Solution()
print(my.firstMissingPositive([5,0,9,-2,3,-1,1]))