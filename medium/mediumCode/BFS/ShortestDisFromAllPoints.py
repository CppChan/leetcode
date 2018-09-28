from collections import deque
class Solution(object):
  def shortestDistance(self, grid):
  	dis,res,shortest= [],[[0]*len(grid[0]) for k in range(len(grid))],float('inf')
  	for i in range(len(grid)):
  		for j in range(len(grid[0])):
  			if grid[i][j]==1:dis.append(self.bfs(i,j,grid[:]))
  	for i in range(len(grid)):
  		for j in range(len(grid[0])):
  			if grid[i][j]!=0:continue
  			complete = True
  			for item in dis:
  				if item[i][j]==float('inf'):
  					complete = False
  					break
  				res[i][j]+=item[i][j]
  			if complete:shortest = min(shortest,res[i][j])
  	if shortest == float('inf'):return -1
  	else:return shortest

  def bfs(self, a,b,grid):
  	tempdis, visited, step= [[float('inf')]*len(grid[0]) for k in range(len(grid))],[[False]*len(grid[0]) for k in range(len(grid))],1
  	queue,tempdis[a][b]= deque([[a,b]]),0
  	while len(queue)>0:
  		start = queue.popleft()
  		i,j= start[0],start[1]
  		if i-1>=0 and grid[i-1][j]==0 and visited[i-1][j]==False:
  			visited[i-1][j],tempdis[i-1][j]=True,tempdis[i][j]+1
  			queue.append([i-1,j])
  		if i+1<len(grid) and grid[i+1][j]==0 and visited[i+1][j]==False:
  			visited[i+1][j],tempdis[i+1][j]=True,tempdis[i][j]+1
  			queue.append([i+1,j])
  		if j-1>=0 and grid[i][j-1]==0 and visited[i][j-1]==False:
  			visited[i][j-1],tempdis[i][j-1]=True,tempdis[i][j]+1
  			queue.append([i,j-1])
  		if j+1<len(grid[0]) and grid[i][j+1]==0 and visited[i][j+1]==False:
  			visited[i][j+1],tempdis[i][j+1]=True,tempdis[i][j]+1
  			queue.append([i,j+1])
  	return tempdis

if __name__=="__main__":
    s = Solution()
    s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,0,0,0]])