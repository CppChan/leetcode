from collections import deque
class Solution(object):
  def numIslands(self, grid):
  	visited, res = [[0]*len(grid[0]) for i in range(len(grid))],0
  	for i in range(len(grid)):
  		for j in range(len(grid[0])):
  			if grid[i][j]=="1":
  				self.bfs(grid, i, j)
  				res+=1
  	return res
  def bfs(self, grid, i, j):
  	queue = deque([(i, j)])
  	while len(queue)>0:
  		start = queue.popleft()
  		i,j= start[0],start[1]
  		for x,y in ((i-1,j),(i+1,j),(i, j-1),(i,j+1)):
  			if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y]=="1":
  				queue.append((x,y))
  				grid[x][y]="*"

if __name__ == "__main__":
    s=Solution()
    print s.numIslands([["1","1","0","0","0"],["0","1","0","0","1"],["1","0","0","1","1"],["0","0","0","0","0"],["1","0","1","0","1"]])
