class Solution(object):
  def maxSum(self, array):
  	if len(array)==1: return [0,0]
  	dp = [[0]*2 for i in range(len(array))]
  	maxval = array[0]*2
  	res = [0,0]
  	for i in range(1,len(array)):
  		temp1,temp2,temp3= 2*array[i], array[i]+array[i-1]+1, array[dp[i-1][0]]+array[i]+i-dp[i-1][0]
  		if temp1>=temp2 and temp1>=temp3: dp[i][0],dp[i][1]=i,i
  		elif temp2>temp1 and temp2>=temp3: dp[i][0],dp[i][1]=i-1,i#corner case >=
  		elif temp3>temp1 and temp3>temp2: dp[i][0],dp[i][1]=dp[i-1][0], i
  		if max(temp1, temp2, temp3)>maxval: maxval,res=max(temp1, temp2, temp3),dp[i]
  	return res