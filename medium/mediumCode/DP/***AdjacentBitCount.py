class Solution(object):
  def getAdjBCStringCount(self, n, k):
  	dp = [[0]*(k+1) for i in range(n+1)]
  	for i in range(1,n+1):
  		for j in range(k+1):
  			if i <= j: dp[i][j]=0
  			elif i == 1 and j == 0: dp[i][j]=2
  			elif i == 2 and j == 0: dp[i][j]=3
  			elif i == 2 and j ==1 : dp[i][j]=1
  			elif j == 0:
  				dp[i][j]=dp[i-1][j]+dp[i-2][j]
  			else:
  				dp[i][j]= dp[i-1][j]+dp[i-1][j-1]+dp[i-2][j]-dp[i-2][j-1]#.....0 + ......11(represent by dp[i-1][j-1]-dp[i-2][j-1]) + ......01
  	return dp[n][k]


class Solution(object):
  def getAdjBCStringCount(self, n, k):
  	if n ==0 and k == 0: return 0
  	dp = [[0]*(k+1) for i in range(n+1)]#remember
  	for i in range(n+1):
  		for j in range(k+1):
  			if i == 0 and j==0: dp[i][j]=1#special case
  			elif i == 0 or (i == 1 and j == 1): dp[i][j]=0
  			elif i == 1 and j == 0: dp[i][j]=2
  			elif i == 2 and j == 0: dp[i][j]=3
  			elif j == 0: dp[i][j]=dp[i-1][0]+dp[i-2][0]
  			else: dp[i][j]=dp[i-1][j]+dp[i-2][j]+dp[i-1][j-1]-dp[i-2][j-1]
  	return dp[n][k]