class Solution:
    def maximumValue(self, strs):
        # count = 0
        # result = 0
        # ans = 0
        # for word in strs:
        #     for i in word:
        #         if i=='0':
        #             continue
        #         else:
        #             count +=1
        #     result = count
        #     count = 0
        #     ans = max(result,ans)
        # return ans4
        max_val = 0 
        for s in strs: 
            if s.isdigit():
                val = int(s) 
            else: val = len(s) 
            max_val = max(max_val, val) 
        return max_val
            
        
        
my = Solution()
print(my.maximumValue(["1","01","001","0001"]))