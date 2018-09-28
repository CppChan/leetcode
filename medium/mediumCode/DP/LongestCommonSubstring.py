class Solution(object):
  def longestCommon(self, s, t):
  	if len(s)==0 or len(t)==0: return ''
  	dp = [[0]*len(t) for i in range(len(s))]
  	res = ''
  	for i in range(len(s)):
  		for j in range(len(t)):
  			if s[i]!=t[j]:continue
  			if (i == 0 and s[i]==t[j]) or (j == 0 and s[i]==t[j]): dp[i][j]=1
  			elif s[i]==t[j]:
  				dp[i][j] = dp[i-1][j-1]+1
  			if dp[i][j]>len(res): res = s[i-dp[i][j]+1: i+1]
  	return res