class Solution(object):
  def longestPalindrome(self, s):
  	if not s or len(s)==0: return ''
  	dp = [['']*len(s) for i in range(len(s))]
  	for k in range(len(s)):
  		for i in range(len(s)-k):
  			j = i+k
  			if i==j:dp[i][j]=s[j]
  			elif j-i==1 and s[j]==s[i]: dp[i][j]=s[i:j+1]
  			else:
  				if s[i]==s[j] and len(dp[i+1][j-1])==(j-1-i):
  					dp[i][j]=s[i]+dp[i+1][j-1]+s[j]
  				else:
  					if len(dp[i+1][j])>len(dp[i][j-1]):dp[i][j]=dp[i+1][j]
  					else:dp[i][j]=dp[i][j-1]
  	return dp[0][len(s)-1]