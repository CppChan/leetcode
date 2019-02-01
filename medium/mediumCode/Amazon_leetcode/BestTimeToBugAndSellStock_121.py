class Solution(object):
    def maxProfit(self, prices):
        lowest, res= float('inf'),0
        for i in range(len(prices)):
            if prices[i]<lowest: lowest = prices[i]
            elif prices[i]>prices[i-1]:
                if prices[i]-lowest>res:res = prices[i]-lowest
        return res