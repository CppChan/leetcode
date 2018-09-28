class Solution(object):
  def firstMissing(self, array):
  	res = 1
  	for i in range(len(array)):#res is the smallest element that can not be represented by element from 0 to i
  		if array[i]<=res:
  			res+=array[i]
  		else: return res
  	return res

#https://www.geeksforgeeks.org/find-smallest-value-represented-sum-subset-given-array/