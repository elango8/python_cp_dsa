class Solution:
    def reverseWords(self, s: str) -> str:
        up_s = s.strip()
        li = []
        st = ""
        for i in range(len(up_s)):
            co = 0
            if up_s[i].isalnum():
                st += up_s[i]
            elif up_s[i] == " ":
                co +=1
                if co <= 1:
                    li.append(st)
                    st = ""
                continue
        if st:
            li.append(st) 
            rev = li[::-1] 
        return " ".join(rev)
my = Solution()
print(my.reverseWords("the sky is blue"))
        
