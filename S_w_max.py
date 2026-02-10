class Solution:
    def maxSlidingWindow(self, nums, k):
        if len(nums) <= 1:
            return nums
        ans = []
        left = 0
        right = k
        for _ in range((len(nums)-k)+1):
            win = nums[left:right]
            ans.append(max(win))
            left +=1
            right +=1
        return ans
            

            
my = Solution()
print(my.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
        
# ans = [3,1,3][1,3,-1,-3,5,3,6,7]
# print(max(ans))