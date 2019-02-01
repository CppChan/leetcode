class Solution(object):
    def coinChange(self, coins, amount):
        if (len(coins)==0 and amount>0) or (amount >0 and amount<min(coins)):return -1# pay attention here !!!
        if amount==0:return 0
        dp = [[0]*len(coins) for i in range(amount+1)]
        mincoin = min(coins)
        coins.sort()
        for i in range(amount+1):
            for j in range(len(coins)):
                if i==0:dp[i][j]=0
                elif i<mincoin: dp[i][j]=float('inf')
                elif j==0:dp[i][j]=dp[i-coins[j]][j]+1
                else:
                    if i<coins[j]:dp[i][j]=dp[i][j-1]
                    else:dp[i][j]=min(dp[i-coins[j]][j]+1, dp[i][j-1])
        if dp[-1][-1]==float('inf'):return -1 # pay attention here !!!
        return dp[-1][-1]