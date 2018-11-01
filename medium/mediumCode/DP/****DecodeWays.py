#consider this question, consider the '0'situation!!
class Solution(object):
  def numDecodeWay(self, s):
  	if len(s)==0 or s[0]=="0":return 0
  	dp = [0]*(len(s)+1)
  	dp[0]=1#corner case !!! if use this dp[0], then there must be one possible assignment
  	for i in range(1,len(dp)):
  		if i == 1:dp[i]=1
  		else:
  			if s[i-1]=='0' and (int(s[i-2])>2 or s[i-2]=='0'):return 0
  			if s[i-1]=='0': dp[i]=dp[i-2]
  			else:
  				if s[i-2]!='0' and int(s[i-2:i])<=26:dp[i]=dp[i-1]+dp[i-2]
  				else: dp[i]=dp[i-1]
  	return dp[len(s)]