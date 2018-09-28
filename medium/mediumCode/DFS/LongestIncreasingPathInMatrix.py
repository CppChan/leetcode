class Solution:
  def longestIncreasingPath(self, matrix):
    res = [0]
    if len(matrix)==0: return res[0]
    dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if dp[i][j]==0:
                self.findway(dp, matrix, i, j, res)
    return res[0]

  def findway(self,dp, matrix, row, col,res):
    up, down, left, right = 0,0,0,0
    if row-1>=0 and matrix[row-1][col]>matrix[row][col]:
        if dp[row-1][col]>0:up = dp[row-1][col]
        else: up = self.findway(dp, matrix, row-1,col,res)
    if row+1<len(matrix) and matrix[row+1][col]>matrix[row][col]:
        if dp[row+1][col]>0:down = dp[row+1][col]
        else:down = self.findway(dp, matrix, row+1,col,res)
    if col-1>=0 and matrix[row][col-1]>matrix[row][col]:
        if dp[row][col-1]>0:left = dp[row][col-1]
        else:left = self.findway(dp, matrix, row,col-1,res)
    if col+1<len(matrix[0]) and matrix[row][col+1]>matrix[row][col]:
        if dp[row][col+1]>0:right = dp[row][col+1]
        else: right =self.findway(dp,matrix, row,col+1,res)
    dp[row][col]=1+max(up, down, left, right)
    if res[0]<dp[row][col]: res[0]=dp[row][col]
    return 1+max(up, down, left, right)