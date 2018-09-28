class Solution(object):
  def largest(self, matrix):
  	up, down,left, right= [[0]*len(matrix[0]) for i in range(len(matrix))],[[0]*len(matrix[0]) for i in range(len(matrix))],[[0]*len(matrix[0]) for i in range(len(matrix))],[[0]*len(matrix[0]) for i in range(len(matrix))]
  	for i in range(len(up)):
  		for j in range(len(up[0])):
  			if i == 0:
  				up[i][j]=matrix[i][j]
  			else:
  				if matrix[i][j]==0:up[i][j]=0
  				else:up[i][j]=up[i-1][j]+1
  	for i in range(len(up)-1,-1,-1):
  		for j in range(len(up[0])):
  			if i == len(up)-1:
  				down[i][j]=matrix[i][j]
  			else:
  				if matrix[i][j]==0:down[i][j]=0
  				else:down[i][j]=down[i+1][j]+1
  	for i in range(len(left[0])):
  		for j in range(len(left)):
  			if i == 0:
  				left[j][i]=matrix[j][i]
  			else:
  				if matrix[j][i]==0:left[j][i]=0
  				else: left[j][i]=left[j][i-1]+1
  	for i in range(len(left[0])-1,-1,-1):
  		for j in range(len(left)):
  			if i == len(left[0])-1:
  				right[j][i]=matrix[j][i]
  			else:
  				if matrix[j][i]==0:right[j][i]=0
  				else: right[j][i]=right[j][i+1]+1
  	res = 0
  	for i in range(len(up)):
  		for j in range(len(up[0])):
  			if matrix[i][j]==0:continue
  			temp = min(up[i][j],down[i][j],left[i][j],right[i][j])
  			if temp>res:res = temp
  	return res

if __name__ == "__main__":

    s = Solution()
    s.largest([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])