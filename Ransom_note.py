from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
  
        dic2 = defaultdict(int)
       
        for ch1 in magazine:
            dic2[ch1] +=1
        for ch in ransomNote:
            if dic2[ch] == 0:  
                return False
            dic2[ch] -= 1     
        return True

        
        
        
my = Solution()
print(my.canConstruct("aa","baa"))