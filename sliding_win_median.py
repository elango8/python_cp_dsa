class Solution:
    def longestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        ans = 1 

        for i in range(n):
            freq = [0] * 26

            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                freq[idx] += 1
                mn = 10**5
                mx = 0
                for c in freq:
                    if c > 0:
                        mn = min(mn, c)
                        mx = max(mx, c)

                if mx == mn:              
                    ans = max(ans, j - i + 1)

        return ans
my = Solution()
print(my.longestBalancedSubstring("zzabccy"))    
