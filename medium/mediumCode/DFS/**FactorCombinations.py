import math
class Solution(object):
  def combinations(self, n):
  	res, temp= [],[]
  	self.dfs(n, 2, temp, res)
  	return res

  def dfs(self, n, start, temp, res):
  	if n<=3:return
  	i = start
  	while i<n:
  		if n%i==0 and n/i>=i:
  			temp.append(i)
  			self.dfs(n/i, i, temp, res)
  			temp.append(n/i)
  			res.append(temp[:])
  			temp.pop(len(temp)-1)
  			temp.pop(len(temp)-1)
  		if n/i<i:break
  		i+=1