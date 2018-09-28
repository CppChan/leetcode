#这一题corner case 很多

class Solution(object):
  def isMatch(self, input, pattern):
  	dp = [[False]*(len(pattern)+1) for i in range(len(input)+1)]
  	if len(input)==0 and len(pattern)==0:return True
  	if (len(input)!=0 and len(pattern)==0):return False
  	dp[0][0]=True
  	for i in range(len(input)+1):
  		for j in range(1,len(pattern)+1):
  			if i == 0 and j == 1: dp[i][j]=False
  			elif i == 0 and j>1:
  				if pattern[j-1]=='*':dp[i][j]=dp[i][j-2]
  			elif j>=1:
  				if j>=2 and pattern[j-1]=='*':
  					dp[i][j]= ((pattern[j-2]==input[i-1] or pattern[j-2] == '.')and (dp[i-1][j-2] or dp[i-1][j])) or dp[i][j-2]#pay attention
  				else:
  					if j<len(pattern) and pattern[j]=='*': dp[i][j]==False
  					elif pattern[j-1]=='.'or pattern[j-1]==input[i-1]: dp[i][j]=dp[i-1][j-1]
  	return dp[len(input)][len(pattern)]


class Solution1(object): # for question Wildcard Matching
  def isMatch(self, input, pattern):
  	dp = [[False]*(len(pattern)+1) for i in range(len(input)+1)]
  	if len(input)==0 and len(pattern)==0:return True
  	if (len(input)!=0 and len(pattern)==0):return False
  	dp[0][0]=True
  	for i in range(len(input)+1):
  		for j in range(1,len(pattern)+1):
  			if i == 0 and j>=1: dp[i][j]=dp[i][j-1] and pattern[j-1]=='*'
  			elif pattern[j-1]=='?'or pattern[j-1]==input[i-1]:dp[i][j] = dp[i-1][j-1]
  			elif pattern[j-1]=='*':dp[i][j]=dp[i-1][j] or dp[i][j-1]#pay attention
  	return dp[len(input)][len(pattern)]


