from collections import defaultdict
class Solution:
    def missingNumber(self, nums) -> int:
        # check_max = len(nums)
        # dix = defaultdict(int)
        # for i in range(check_max+1):
        #     dix[i] = 1 if i in nums else 0

        # for j,k in dix.items():
        #     if k == 0:
        #         return j
        n = len(nums)
        s = set(nums)
        for i in range(n+1):  
            if i not in s:
                return i
            
my = Solution()    
print(my.missingNumber([0,1]))