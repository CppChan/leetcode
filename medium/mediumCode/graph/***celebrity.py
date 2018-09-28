class Solution(object):
  def celebrity(self, matrix):
  	kong, index, iskong= 0,0,True
  	if len(matrix)==0:return -1
  	for i in range(len(matrix)):
  		iskong = True
  		for j in range(len(matrix[0])):
  			if j==i:continue #corner case!!
  			if matrix[i][j]==1:iskong=False
  		if iskong:
  			kong+=1
  			index = i
  	if kong!=1:return -1
  	for i in range(len(matrix)):
  		if i == index:continue
  		if matrix[i][index]==0:return -1
  	return index