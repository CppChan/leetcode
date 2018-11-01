
# cannot use step , because we should add up step after going through a level but not a node
from collections import deque
class Solution(object):
  def wallsAndGates(self, rooms):
  	queue = deque([])
  	for i in range(len(rooms)):
  		for j in range(len(rooms[0])):
  			if rooms[i][j] == 0: queue.append((i,j)) # here is the first level !!
  	distance = 1
  	while len(queue)>0:
  		start = queue.popleft()
  		i, j = start[0],start[1]
  		for x,y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
  			if x>=0 and x<len(rooms) and y>=0 and y<len(rooms[0]) and rooms[x][y] == 2147483647:
  				rooms[x][y] = rooms[i][j]+1
  				queue.append((x,y))

# from collections import deque
# class Solution(object):
#   def wallsAndGates(self, rooms):
#   	for i in range(len(rooms)):
#   		for j in range(len(rooms[0])):
#   			if rooms[i][j]==0: self.findpath(rooms, i, j)
#   	return rooms
#
#   def findpath(self, rooms, a, b):
#   	visited, queue, step= [[False]*len(rooms[0]) for k in range(len(rooms))], deque([[a,b]]),1
#   	while len(queue)>0:
#   		start= queue.popleft()
#   		i,j= start[0], start[1]
#   		if i-1>=0 and rooms[i-1][j]!=-1 and rooms[i-1][j]!=0 and not visited[i-1][j]:
#   			rooms[i-1][j]=min(rooms[i-1][j], rooms[i][j]+1)#cannot rooms[i-1][j]=min(rooms[i-1][j], step)
#   			visited[i-1][j]=True
#   			queue.append([i-1,j])
#   		if i+1<len(rooms) and rooms[i+1][j]!=-1 and rooms[i+1][j]!=0and not visited[i+1][j]:
#   			rooms[i+1][j]=min(rooms[i+1][j], rooms[i][j]+1)
#   			visited[i+1][j]=True
#   			queue.append([i+1,j])
#   		if j-1>=0 and rooms[i][j-1]!=-1 and rooms[i][j-1]!=0 and not visited[i][j-1]:
#   			rooms[i][j-1]=min(rooms[i][j-1], rooms[i][j]+1)
#   			visited[i][j-1]=True
#   			queue.append([i,j-1])
#   		if j+1<len(rooms[0]) and rooms[i][j+1]!=-1 and rooms[i][j+1]!=0 and not visited[i][j+1]:
#   			rooms[i][j+1]=min(rooms[i][j+1], rooms[i][j]+1)
#   			visited[i][j+1]=True
#   			queue.append([i,j+1])
		#step+=1  # cannot use step , because we should add up step after going through a level but not a node

if __name__=="__main__":
    s = Solution()
    print s.wallsAndGates([[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]])