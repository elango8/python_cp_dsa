class Solution:
    def twoSum(self, numbers, target: int):
        L = 0
        R = len(numbers)-1
        sum = 0
        while L < R:
            sum = numbers[L]+ numbers[R]
            if sum > target:
                R -=1
            elif sum < target:
                L +=1
            elif sum == target:
                return [L+1,R+1]
   
my = Solution()
print(my.twoSum([-1,0],-1))