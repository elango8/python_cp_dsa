from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int)
        for ch in s:
            dic[ch] +=1
        sorting = sorted(dic.items(),key=lambda x:(-x[1],x[0]))
        result = ""
        for fre,wor in sorting:
            re = fre*wor
            result += re
        return result
        
out = Solution()
print(out.frequencySort("tree"))