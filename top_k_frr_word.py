import heapq
from collections import defaultdict
class Solution():
    def fre_word(self,nums,k):
        dic = defaultdict(int)
        for num in nums:
            dic[num] +=1
        res = []
        for ke,fre in dic.items():
            heapq.heappush(res,(fre,ke))
            if len(res) > k:
                heapq.heappop(res)
            
        res.sort(key=lambda x:(-x[0],x[1]))
        result =[]
        for fre,wor in res:
            result.append(wor)
        return result
        
my = Solution()
print(my.fre_word(["i","love","leetcode","i","love","coding"],1))
