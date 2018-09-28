class Solution(object):
  def editDistance(self, one, two):
  	dp = [[0]*(len(two)+1) for i in range(len(one)+1)]
  	for i in range((len(one)+1)):
  		for j in range((len(two)+1)):
  			if i == 0:dp[0][j]=j
  			if j == 0:dp[i][0]=i
  			elif i!=0 and j!=0:
  				if one[i-1]==two[j-1]:dp[i][j]=dp[i-1][j-1]
  				else:dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
  	return dp[len(one)][len(two)]


if __name__ == "__main__":
    # s = Solution()
    # print s.editDistance("a", "")
	a = 'a'
	print int(a)