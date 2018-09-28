class Solution(object):
  def coinChange(self, coins, amount):
    if len(coins)==0:
        if amount == 0: return 0
        else: return -1
    coins = sorted(coins)
    dp = [[0]*len(coins) for i in range(amount+1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0: dp[i][j]=0
            elif j == 0:
                if i%coins[j]!=0:dp[i][j]=float('inf')#dont write float['inf']
                else: dp[i][j]=i/coins[j]
            else:
                if coins[j]>i: dp[i][j]=dp[i][j-1]
                else: dp[i][j]=min(dp[i-coins[j]][j]+1, dp[i][j-1])
    if dp[amount][len(coins)-1]==float('inf'): return -1
    else: return dp[amount][len(coins)-1]