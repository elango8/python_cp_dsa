class Solution:
    def maxSumTrionic(self, nums) -> int:
        n= len(nums)
        if n < 4:
            return 0
        i = 0
        if nums[0] > nums[1]:
            i += 1
        j = i

        while nums[j] < nums[j+1]:
            j+=1
        p = j
        while nums[j] > nums[j+1]:
            j+=1
        q = j
        l = p-1
        r = q+1
        return p,q,l,r  
my = Solution()
print(my.maxSumTrionic([0,-2,-1,-3,0,2,-1]))      