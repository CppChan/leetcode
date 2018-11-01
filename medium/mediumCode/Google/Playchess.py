class Solution(object):
  def find(self, input):
  	visited, point= [[0]*len(input[0]) for i in range(len(input))],[0,0]
  	for i in range(len(input)):
  		for j in range(len(input[0])):
  			if self.canWin(i, j, input, point, visited,0, True): return (i,j)
  	return None

  def canWin(self, i, j, input, point, visited, step, my):
  	if step == len(input)*len(input[0]):
  		if my:
  			if point[0]>point[1]:return True
  			else:return False
  		else:
  			if point[1]>point[0]:return True
  			else:return False
  	for x,y in ((i-1,j),(i+1,j), (i, j-1), (i,j+1)):
  		if x>=0 and x<len(input) and y>=0 and y<len(input[0]):
  			pre_visit = visited[x][y]
  			if not visited[x][y]:
  				if my: point[0]+=input[x][y]
  				else: point[1]+=input[x][y]
  				visited[x][y]=1
  			if self.canWin(self, x,y, input, point, visited, step+1, not my): return False
  			visited[x][y]=pre_visit
  			if pre_visit == 0:
  				if my: point[0]-=input[x][y]
  				else: point[1]-=input[x][y]
  		return True

s = Solution()
print s.find([[1,1],[1,3]])



