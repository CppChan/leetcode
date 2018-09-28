class Solution(object):
  def search(self, matrix, target):
  	if len(matrix)==0: return [-1,-1]
  	row,col = len(matrix), len(matrix[0])
  	start, end, mid= 0, row-1,0
  	while start<end-1:
  		mid = (start+end)/2
  		if target>matrix[mid][0]:start = mid
  		elif matrix[mid][0]>target: end = mid
  		else: return [mid, 0]
  	if target>=matrix[row-1][0]:start = row-1#corner case!!!!!, because matrix[row-1]canbe <=target
  	begin, last,mid = 0, col-1,0
  	while begin<last:
  		mid = (begin+last)/2
  		if target>matrix[start][mid]:begin= mid+1
  		elif matrix[start][mid]>target: last= mid-1
  		else:return[start,mid]
  	if matrix[start][begin]==target:return [start, begin]
  	return[-1,-1]