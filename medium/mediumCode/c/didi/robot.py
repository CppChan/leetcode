class Solution(object):
    def pathnum(self, input):
        if len(input)==0 or input[0][0]==1 or input[len(input)-1][len(input[0])-1]==1: return 0
        dp = [[0]*len(input[0]) for i in range(len(input))]
        for i in range(len(input)):
            for j in range(len(input[0])):
                if i==0 and j==0: dp[i][j]=1
                elif input[i][j]==1:dp[i][j]=0
                elif i == 0: dp[i][j]=dp[i][j-1]
                elif j==0: dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[len(input)-1][len(input[0])-1]


s = Solution()
print s.pathnum([[0,0,0],[0,1,0],[0,0,0]])