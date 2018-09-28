class Solution(object):
	def largest(self, matrix):
		dp = [[0]*len(matrix) for g in range(len(matrix))]
		res = 0
		for i in range(len(matrix)):
			for j in range(len(matrix)):
				if i == 0 or j == 0:
					if matrix[i][j]==1:
						dp[i][j]=1
						if 1>res:
							res = 1
				else:
					if matrix[i][j]==0:
						dp[i][j]=0
						continue
					prelen = dp[i-1][j-1]
					curlen = 1
					for k in range(1,prelen+1):
						if matrix[i-k][j]==1 and matrix[i][j-k]==1:
							curlen+=1
						else:
							break
					dp[i][j]=curlen
					if curlen>res:
						res = curlen
		return res