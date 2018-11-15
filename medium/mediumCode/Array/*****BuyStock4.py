# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java

class Solution(object):
    def maxProfit(self, k, profit):
        if len(profit) == 0 or len(profit) == 1:
            return 0
        if k > ((len(profit)) / 2):
            return self.quick(profit)
        dp = [[0] * len(profit) for i in range(k + 1)] # max income by certain day using certain time transactions
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



if __name__ == "__main__":
    s = Solution()
    print s.maxProfit(2,[3,3,5,0,0,3,1,4])