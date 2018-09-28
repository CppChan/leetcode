from collections import deque
class Solution(object):
  def numIslands(self, grid):
  	if len(grid)==0:return 0
  	visited,res= [[False]*len(grid[0]) for i in range(len(grid))],0
  	for i in range(len(grid)):
  		for j in range(len(grid[0])):
  			if grid[i][j]=="1" and not visited[i][j]:
  				self.bfs(grid, visited, i, j)
  				res+=1
  	return res

  def bfs(self, grid, visited, i, j):
  	queue = deque([[i,j]])
  	while len(queue)>0:
  		start = queue.popleft()
  		a, b = start[0], start[1]
		if a>=0 and a<len(grid) and b>=0 and b<len(grid[0]) and not visited[a][b] and grid[a][b]=='1':
			visited[a][b]=True
			queue.extend([a-1,b],[a+1][b],[a,b-1],[a,b+1])

if __name__ == "__main__":
    s=Solution()
    print s.numIslands([["1","1","0","0","0"],["0","1","0","0","1"],["1","0","0","1","1"],["0","0","0","0","0"],["1","0","1","0","1"]])
