class Solution(object):
  def numOfTriangles(self, array):
  	res = 0
  	for i in range(len(array)):
  		if array[i]<=0:
  			array.pop(i)
  			i-=1
  	array = sorted(array)
  	for i in range(len(array)-2):
  		k = i+2
  		for j in range(i+1, len(array)-1):
  			while k<len(array) and array[i]+array[j]>array[k]:# here, k unchanged!!
  				k+=1
  			res+=k-j-1
  	return res