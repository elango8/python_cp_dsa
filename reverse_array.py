class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        r = len(s)-1
        while r > l:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp
                l +=1
                r -= 1
        return s
my = Solution()
print(my.reverseString(["h","e","l","l","o"]))