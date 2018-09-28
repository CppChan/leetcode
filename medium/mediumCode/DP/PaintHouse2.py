class Solution(object):
  def minCostII(self, costs):
    tempmin = (float('inf'),float('inf'))
    tempsecond = (float('inf'),float('inf'))
    dp= [[0]*len(costs[0]) for i in range(len(costs))]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0:
                dp[i][j] = costs[i][j]
            else:
                if j == tempmin[1]: dp[i][j]=costs[i][j]+tempsecond[0]
                else: dp[i][j]=costs[i][j]+tempmin[0]
        tempmin = (float('inf'),float('inf'))
        tempsecond = (float('inf'),float('inf'))
        for j in range(len(dp[0])):
            if dp[i][j]<=tempmin[0]:
                tempsecond = tempmin
                tempmin =(dp[i][j],j)
            elif dp[i][j]<tempsecond[0]:
                tempsecond = (dp[i][j],j)
    res = float('inf')
    for j in range(len(dp[0])):
        if dp[-1][j]<res: res = dp[-1][j]
    return res