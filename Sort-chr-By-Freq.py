from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int)
        for ch in s:
            dic[ch] +=1
        
        
out = Solution()
print(out.frequencySort("Aabb"))