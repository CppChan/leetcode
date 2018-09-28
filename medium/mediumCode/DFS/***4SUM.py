class Solution(object):
  def fourSum(self, array, target):
  	array = sorted(array)
  	res = []
  	if len(array)<4: return res
  	self.findsum(array, target, 4, res, [])
  	return res

  def findsum(self, array, target, N, res, tempres):

  	if N == 2:#solve 2sum
  		if len(array)<2:return
  		l, r = 0, len(array)-1
  		while l<r:
  			if (l == 0 or array[l]!=array[l-1]) and (r == len(array)-1 or array[r]!=array[r+1]):
  				if array[l]+array[r] == target:
  					res.append(tempres+[array[l], array[r]])
  					l+=1
  				elif array[l]+array[r]<target:l+=1
  				else:r-=1
  			else:
  				if l!=0 and array[l]==array[l-1]:l+=1
  				if r!=len(array)-1 and array[r]==array[r+1]:r-=1
  		return
  	else:#solve nSum(n>2)
  		if array[0]*N>target or array[-1]*N<target:
  			return
  		for i in range(0, len(array)-N+1):
  			if i == 0 or array[i]!=array[i-1]:self.findsum(array[i+1:len(array)], target-array[i], N-1, res, tempres+[array[i]])

