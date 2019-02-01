class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [0]*(len(cost)+1)
        if len(dp)==2:return cost[0]
        for i in range(len(dp)):
            if i==0: dp[i]=0
            elif i == 1: dp[i]=0
            elif i == 2: dp[i]=min(cost[0], cost[1])
            else:
                dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[-1]