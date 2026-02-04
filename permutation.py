from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h = len(s1)-1
        d1 = defaultdict(int)
        while h >= 0:
            d1[s1[h]] +=1
            h -=1
        
        d2 = defaultdict(int)
        win = len(s1)
        for i in range(len(s2)):
            d2[s2[i]] +=1
            if i >= len(s1):
                left = s2[i-win]
                d2[left] -=1
                if d2[left] == 0:
                    del d2[left]
            if d1 == d2:
                return True
        
        return False
        
            
        
me = Solution()
print(me.checkInclusion("ab", "eidbaooo"))