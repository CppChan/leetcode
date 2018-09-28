class Solution(object):
  def whiteObjects(self, matrix):
  	if len(matrix)==0 or len(matrix[0])==0:
  		return 0
  	isVisited = [[False]*len(matrix[0]) for g in range(len(matrix))]
  	res = 0
  	for i in xrange(len(matrix)):
  		for j in xrange(len(matrix[0])):
  			if isVisited[i][j]==True:
  				continue
  			if matrix[i][j]==0:
  				self.expand(matrix, isVisited, i, j)
  				res+=1
  	return res

  def expand(self, matrix, isVisited, i, j):
  	if i<0 or i >=len(matrix) or j<0 or j>=len(matrix[0]):
  		return
  	elif isVisited[i][j]== True:
  		return
  	elif matrix[i][j]==1:
  		isVisited[i][j]= True
  	elif matrix[i][j]==0:
  		isVisited[i][j]= True
  		self.expand(matrix, isVisited, i-1, j)
  		self.expand(matrix, isVisited, i+1, j)
  		self.expand(matrix, isVisited, i, j-1)
  		self.expand(matrix, isVisited, i, j+1)


if __name__ == "__main__":
    s =Solution()
    print s.whiteObjects([[0,0,0,1],[1,0,1,1],[1,1,0,0],[0,1,0,0]])