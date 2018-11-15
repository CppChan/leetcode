class Solution(object):
  def find(self, matrix,target):
  	if len(matrix)==0 or target<matrix[0][0] or target>matrix[-1][-1]:return None
  	i,j=0,len(matrix[0])-1
  	while i<len(matrix) and j>0:
  		if matrix[i][j]==target:return (i,j)
  		elif matrix[i][j]>target:j-=1
  		else: i+=1
  	return None