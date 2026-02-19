from collections import defaultdict
class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        dic = defaultdict(int)
        for i in range(n):
            dic[nums[i]] +=1
        return max(dic,key = dic.get)
        
  
  
my = Solution()
print(my.majorityElement([2,1,1,1,2]))      