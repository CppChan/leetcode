class Solution(object):
  def minJump(self, array):
  	if len(array)==1:return 0
  	dp, nearest= [-1]*len(array), len(array)-1
  	for i in range(len(array)-1,-1,-1):
  		if i == len(array)-1:dp[i]=0
  		else:
  			if nearest-i<=array[i]:
  				nearest = i
  				temp = float('inf')
  				for j in range(nearest, nearest+array[i]+1):
  					if j<len(array) and dp[j]>-1:temp = min(temp,dp[j])
  				dp[i]=temp+1
  			else: dp[i]=-1
  	return dp[0]


