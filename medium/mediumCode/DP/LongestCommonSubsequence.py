class Solution(object):
  def longest(self, s, t):
  	if len(s)==0 or len(t)==0: return 0
  	dp = [[0]*len(t) for i in range(len(s))]
  	for i in range(len(s)):
  		for j in range(len(t)):
  			if (i == 0 and s[i]==t[j]) or (j == 0 and s[i]==t[j]): dp[i][j]=1
  			elif s[i]==t[j]:
  				dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
  			elif s[i]!=t[j]:
  				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  	return dp[len(s)-1][len(t)-1]