class Solution(object):
  def exist(self, matrix,cand):
  	if len(cand)==0:return True
  	if len(matrix)==0 and len(cand)!=0:return False
  	for i in range(len(matrix)):
  		for j in range(len(matrix[0])):
  			if self.dfs(cand, matrix, 0, i, j):return True
  	return False
  def dfs(self, word, matrix, k, i, j):
  	if matrix[i][j]!=word[k]:return False
  	if k == len(word)-1: return True
  	matrix[i][j]+="*" # dont need to use visit
  	if i>0 and self.dfs(word, matrix, k+1, i-1, j):return True
  	if i<len(matrix)-1 and self.dfs(word, matrix, k+1, i+1, j):return True
  	if j>0 and self.dfs(word, matrix, k+1, i, j-1):return True
  	if j<len(matrix[0])-1 and self.dfs(word, matrix, k+1, i, j+1):return True
  	matrix[i][j]=matrix[i][j][:1]
  	return False

