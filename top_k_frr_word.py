import heapq
from collections import defaultdict
class Solution():
    def fre_word(self,nums,k):
        dic = defaultdict(int)
        for num in nums:
            dic[num] +=1
        res = []
        for ke,fre in dic.items():
            heapq.heappush(res,(-fre,ke))
            if len(res) > k:
                heapq.heappop(res)
            
        result =[]
        while res:
            result.append(heapq.heappop(res)[1])
        return result
        
        
my = Solution()
print(my.fre_word(["the","day","is","sunny","the","the","the","sunny","is","is"],4))