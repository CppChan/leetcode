class Solution(object):
  def leastInsertion(self, input):
  	if len(input)==0: return 0
  	dp= [[0]*len(input) for i in range(len(input))]
  	for k in range(len(input)):
  		for i in range(len(input)-k):
  			j = i+k
  			if i==j: dp[i][j]=1
  			elif i==j-1:
  				if input[i]==input[j]:dp[i][j]=2
  				else:dp[i][j]=1
  			else:
  				if input[i]==input[j]: dp[i][j]=2+dp[i+1][j-1]
  				else:dp[i][j]=max(dp[i+1][j],dp[i][j-1])
  	return len(input)-dp[0][len(input)-1]