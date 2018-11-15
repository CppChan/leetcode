class Solution(object):
	def canPartition(self, input):
		total,mindif=0,float('inf')
		for i in range(len(input)):
			total+=input[i]
		dif, dp, issum= float('inf'), [[False]*len(input) for i in range(total+1)], [False]*total
		for i in range(len(dp)):
			for j in range(len(dp[0])):
				if i==0: dp[i][j]=True
				elif j==0 and i>0: dp[i][j]=False
				else:
					if i>=input[j]: dp[i][j]=dp[i-input[j]][j-1]
					dp[i][j]=dp[i][j] or dp[i][j-1]
				if dp[i][j]: issum[i]=True
		for s in range(len(issum)):
			if issum[s] and abs(s-(total-s))<mindif: mindif = abs(s-(total-s))
		return mindif


if __name__=="__main__":
    s = Solution()
    print s.canPartition([1,2,3,4,5])