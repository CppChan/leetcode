class Solution(object):
  def numWays(self, n, k):
    pre = 0
    dp = [[0]*k for i in range(n)]
    for i in range(n):
        temppre = 0
        for j in range(k):
            if i == 0:
                dp[i][j]=1
            elif i == 1:
                dp[i][j]=pre
            elif i == 2:
                dp[i][j]=pre-1
            else:
                dp[i][j]=pre-dp[i-3][j](k-1)
            temppre+=dp[i][j]
        pre = temppre
    return pre

#better solution

class Solution(object):
  def numWays(self, n, k):
    dp = [0]*n
    for i in range(n):
        if i == 0:
            dp[i]=k
        elif i == 1:
            dp[i]=k*k
        else:
            dp[i]=(k-1)*(dp[i-1]+dp[i-2])
    return dp[-1]