class Solution:
    def maxProfit(self, prices):
        budget = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < budget:
                budget = prices[i]
            profit = max(profit,prices[i]-budget)
        return profit
        
 
my = Solution()
print(my.maxProfit([7,1,5,3,6,4]))       