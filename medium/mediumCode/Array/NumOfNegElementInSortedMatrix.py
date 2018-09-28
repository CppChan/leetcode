class Solution(object):
  def negNumber(self, matrix):
  	if len(matrix)==0: return 0
  	i, j,prej = len(matrix)-1,0,0
  	res = 0
  	while i>=0 and j<=len(matrix[0]):
  		while i>0 and matrix[i][j]>0 :
  			i-=1
  		if matrix[i][j]>0: break
  		while j < len(matrix[0])-1 and matrix[i][j]<0:
  			j+=1
  		if matrix[i][j]<0:
  			res+=(i+1)*(j-prej+1)
  			break
  		else: res+=(j-prej)*(i+1)
  		prej = j
  	return res