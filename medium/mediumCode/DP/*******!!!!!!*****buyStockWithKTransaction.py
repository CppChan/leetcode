class Solution(object):
    def maxProfit(self, profit, k):
        if k > (len(profit)) / 2:
            self.quick(profit)
        dp = [[0] * len(profit) for i in range(k + 1)]
        for i in range(1, len(dp)):
            tm = -profit[0]
            for j in range(1, len(dp[0])):
                dp[i][j] = max(dp[i][j - 1], profit[j] + tm)
                tm = max(tm, dp[i - 1][j - 1] - profit[j])
        return dp[k][len(profit) - 1]

    def quick(self, profit):
        res = 0
        for i in range(1, len(profit)):
            if profit[i] > profit[i - 1]:
                res += (profit[i] - profit[i - 1])
        return res


# Easy to understand explanation for the above solution
#
# dp[i][j] = maximum profit from at most i transactions using prices[0..j]
#
# A transaction is defined as one buy + sell.
#
# Now on day j, we have two options
#
# Do nothing (or buy) which doesn't change the acquired profit : dp[i][j] = dp[i][j-1]
#
# Sell the stock: In order to sell the stock, you must've bought it on a day t=[0..j-1]. Maximum profit that can be attained is t:0->j-1 max(prices[j]-prices[t]+dp[i-1][t-1]) where prices[j]-prices[t] is the profit from buying on day t and selling on day j. dp[i-1][t-1] is the maximum profit that can be made with at most i-1 transactions with prices prices[0..t-1].
#
# Time complexity of this approach is O(n2k).
#
# In order to reduce it to O(nk), we must find t:0->j-1 max(prices[j]-prices[t]+dp[i-1][t-1]) this expression in constant time. If you see carefully,
#
# t:0->j-1 max(prices[j]-prices[t]+dp[i-1][t-1]) is same as
#
# prices[j] + t:0->j-1 max(dp[i-1][t-1]-prices[t])
#
# Second part of the above expression maxTemp = t:0->j-1 max(dp[i-1][t-1]-prices[t]) can be included in the dp loop by keeping track of the maximum value till j-1.
#
# Base case:
#
# dp[0][j] = 0; dp[i][0] = 0
#
# DP loop:
#
# for i : 1 -> k
#     maxTemp = -prices[0];
#     for j : 1 -> n-1
#         dp[i][j] = max(dp[i][j-1], prices[j]+maxTemp);
#         maxTemp = max(maxTemp, dp[i-1][j-1]-prices[j]);
# return dp[k][n-1];


#!!!!!!!!!General method

class General(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1: return 0
        dp = [0] * len(prices)
        temp = -prices[0]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], prices[i] + temp)#same as before
            temp = max(temp, dp[i - 1] - prices[i])
        return dp[-1]

class BestTimeWithCoolDown(object):
    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1: return 0
        dp = [0] * len(prices)
        temp = -prices[0]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], prices[i] + temp)
            if i == 1:temp = max(temp, -prices[i]) #here is different with General one
            else:temp = max(temp, dp[i - 2] - prices[i])
        return dp[-1]

class GeneralWith2MaxTransaction:
    def maxProfit(self, profit):
        k = 2
        if len(profit) == 0 or len(profit) == 1:
            return 0
        if k >= ((len(profit)) / 2):
            return self.quick(profit)
        dp = [[0] * len(profit) for i in range(k + 1)]
        for i in range(1, len(dp)):
            tm = -profit[0]
            for j in range(1, len(dp[0])):
                dp[i][j] = max(dp[i][j - 1], profit[j] + tm)
                tm = max(tm, dp[i - 1][j - 1] - profit[j])
        return dp[k][len(profit) - 1]

    def quick(self, profit):
        res = 0
        for i in range(1, len(profit)):
            if profit[i] > profit[i - 1]:
                res += (profit[i] - profit[i - 1])
        return res
