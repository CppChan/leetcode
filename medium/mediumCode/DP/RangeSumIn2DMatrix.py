class Solution(object):
    def sumRegion(self, matrix, row1, col1, row2, col2):
        if len(matrix)==0: return 0
        dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and j == 0: dp[i][j]=matrix[i][j]
                elif i == 0: dp[i][j]=dp[i][j-1]+matrix[i][j]
                elif j == 0: dp[i][j]=dp[i-1][j]+matrix[i][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+matrix[i][j]
        return dp[row2][col2]-dp[row1-1][col2]-dp[row2][col1-1]+dp[row1-1][col1-1]
