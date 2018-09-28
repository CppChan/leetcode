#consider this question, consider the '0'situation!!

class Solution(object):
  def numDecodeWay(self, s):
  	if len(s)<1 or (int(s[0:1])==0):return 0
  	dp = [0]*(len(s)+1)
  	dp[0]=1
  	dp[1]=1
  	for i in range(2,len(s)+1):
  		if (int(s[i-2:i])<=26 and int(s[i-2:i-1])!=0):#PAY attention!!, consider '01'situation
  			if int(s[i-1:i])==0:
  				dp[i]=dp[i-2]
  			else:
  				dp[i]=dp[i-1]+dp[i-2]
  		else:
  			if int(s[i-1:i])==0:# this is '50'situation
  				return 0
  			dp[i]=dp[i-1]
  	return dp[len(s)]