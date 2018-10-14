class Solution(object):
  def longest(self, matrix):
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


  def longest2(self, matrix):
  	dp = [[0]*len(matrix[0]) for i in range(len(matrix))]
  	res  = [0]
  	if len(matrix)==0:return 0
  	for i in range(len(matrix)):
  		for j in range(len(matrix[0])):
  			if (i == 0 or matrix[i-1][j]>=matrix[i][j])and (i==len(matrix)-1 or matrix[i+1][j]>=matrix[i][j]) and (j==0 or  matrix[i][j-1]>=matrix[i][j]) and (j==len(matrix[0]) or matrix[i][j+1]>=matrix[i][j]):
  				self.dfs(matrix, dp, i, j, res, 0, 1)
  	return res[0]

  def dfs(self, matrix, dp, i, j, res, direct, step):
  	if dp[i][j]>=step: return
  	dp[i][j]=max(dp[i][j], step)
  	res[0]=max(res[0],dp[i][j])
  	if direct !=1 and i-1>=0 and matrix[i-1][j]>matrix[i][j]:
  		self.dfs(matrix, dp, i-1,j, res, 3, step+1)
  	if direct !=2 and j+1<len(matrix[0]) and matrix[i][j+1]>matrix[i][j]:
  		self.dfs(matrix,dp,i, j+1, res, 4, step+1)
  	if direct !=3 and i+1<len(matrix) and matrix[i+1][j]>matrix[i][j]:
  		self.dfs(matrix, dp, i+1,j, res, 1, step+1)
  	if direct !=4 and j-1>=0 and matrix[i][j-1]>matrix[i][j]:
  		self.dfs(matrix,dp,i, j-1, res, 2, step+1)