class Solution(object):
  def longestPalindrome(self, s):
  	if not s or len(s)==0: return ''
  	dp = [[False]*len(s) for i in range(len(s))]
  	res = ''
  	for k in range(len(s)):
  		for i in range(len(s)-k):
  			j = i+k
  			if i==j:dp[i][j]=True
  			elif j-i==1 and s[j]==s[i]: dp[i][j]=True
  			else:
  				if s[i]==s[j] and dp[i+1][j-1]==True:
  					dp[i][j]=True
  				else:dp[i][j]=False
  			if dp[i][j] and j-i+1>len(res):res = s[i:j+1]
  	return res