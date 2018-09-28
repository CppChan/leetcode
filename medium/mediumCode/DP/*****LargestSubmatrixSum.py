class Solution(object):
  def largest(self, matrix):
  	rowsum = [[0]*len(matrix[0]) for i in range(len(matrix)+1)]
  	for i in range(len(rowsum)):#making a row sum matrix, row3-row1 = matrix sum of 1-3 row
  		for j in range(len(rowsum[0])):
  			if i == 0 :continue
  			rowsum[i][j]=rowsum[i-1][j]+matrix[i-1][j]
  	res = 0
  	for i in range(len(rowsum)-1):
  		for j in range(i+1, len(rowsum)):
  			temp = [0]*len(rowsum[0])
  			for k in range(len(rowsum[0])):
  				temp[k]=rowsum[j][k]-rowsum[i][k]
  			tempres = self.largestSum(temp)
  			if tempres>res:res = tempres
  	return res

  def largestSum(self, array):
    res = -float('inf')
    if len(array)==0:
      return 0
    pre = [0]*len(array)
    pre[0]=array[0]
    for i in range(1,len(array)):
      if pre[i-1]<=0:
        pre[i]=array[i]
      else:
        pre[i]=pre[i-1]+array[i]
    for j in pre:
      res = max(res, j)
    return res