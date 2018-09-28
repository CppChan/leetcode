class Solution(object):
  def numIslands(self, grid):
  	if len(grid)==0:return 0
  	isvisit, res= [[0]*len(grid[0]) for i in range(len(grid))],0
  	for i in range(len(grid)):
  		for j in range(len(grid[0])):
  			if grid[i][j]=='1' and not isvisit[i][j]:
  				self.dfs(isvisit, grid, i, j, 0)
  				res+=1
  	return res

  def dfs(self, isvisit, grid, i,j, direct):
  	if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0' or (grid[i][j]=='1' and isvisit[i][j]==1):return
  	isvisit[i][j]=1
  	if direct != 1:self.dfs(isvisit, grid, i-1,j,3)# remember to avoid the previous direction , ow will cause death recursion
  	if direct != 3:self.dfs(isvisit, grid, i+1,j,1)
  	if direct != 4:self.dfs(isvisit, grid, i,j-1,2)
  	if direct != 2:self.dfs(isvisit, grid, i,j+1,4)