class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        con = set()
        for num in nums:
            con.add(num)
        lar_sub = 1
        for n in con:
            if n-1 in con:
                continue
            else:
                curr_num = n
                curr_sub = 1
                while 1+curr_num in con:
                    curr_num +=1
                    curr_sub +=1
                lar_sub = max(curr_sub,lar_sub)
        return lar_sub
        
my = Solution()
print(my.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))