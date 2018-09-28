class Solution(object):
  def numOfTrees(self, n):
  	if n < 1: return 1
  	return self.findTree(1,n)

  def findTree(self, start, end):
  	sum = 0
  	if start>end:return 0
  	if start == end:return 1
  	for i in range(start, end+1):
  		if self.findTree(start, i-1) ==0:
  			sum+=self.findTree(i+1,end)
  		elif self.findTree(i+1,end) == 0:
  			sum+=self.findTree(start, i-1)
  		else:
  			sum+=self.findTree(start, i-1)*self.findTree(i+1,end)
  	return sum