from collections import defaultdict
class Solution:
    def rotateRight(self, nums):
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] +=1
        for val,dup in dic.items():
            if dup > 1:
                return val 
            
        
my = Solution()
print(my.rotateRight([1,2,3,3,4,5]))
        