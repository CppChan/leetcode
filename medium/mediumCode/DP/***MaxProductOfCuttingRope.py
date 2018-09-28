class Solution(object):
  def maxProduct(self, length):
  	dp = [0]*length
  	if length<=2: return 1
  	dp[0]=1
  	for i in range(1,length):
  		temp = -float('inf')
  		for j in range(1,i+1):
  			temp = max(temp, j*dp[i-j], j*(i-j+1))#j*(i-j+1) corner case
  		dp[i]=temp
  	return dp[length-1]