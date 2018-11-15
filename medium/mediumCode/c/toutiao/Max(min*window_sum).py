class Solution(object):
	def find(self, input):
		minlist,dp, res= [[0]*len(input) for i in range(len(input))],[[0]*len(input) for i in range(len(input))], 0
		for k in range(len(input)):
			for i in range(len(input)-k):
				j = i+k
				if i == j:
					minlist[i][j], dp[i][j]=input[i], input[i]
				else:
					minlist[i][j] = min(input[i],minlist[i+1][j])
					dp[i][j]= dp[i+1][j]+input[i]
				res = max(res, minlist[i][j]*dp[i][j])
		return res


if __name__=="__main__":
    s = Solution()
    print s.find([3,1,6,4,5])