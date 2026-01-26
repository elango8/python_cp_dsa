import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums, k: int):
        dic = defaultdict(int)
        for num in nums:
            dic[num] +=1   
        res = []
        for no,fre in dic.items():
            heapq.heappush(res,(fre,no))
        while len(res) > k:
            heapq.heappop(res)   
        
        result =[]
        i = len(res)-1
        while i >= 0:
            result.append(res[i][1])
            i -=1
        return result[::-1]
             
            
my = Solution()
print(my.topKFrequent([3,0,1,0],1)) 