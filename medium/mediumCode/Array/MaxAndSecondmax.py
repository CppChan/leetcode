class Solution(object):
  def largestAndSecond(self, array):
  	if array[0]>array[1]:
  		first = array[0]
  		second = array[1]
  	else:
  		first = array[1]
  		second = array[0]
  	res = []
  	for i in range(1,len(array)):
  		if array[i]>first:
  			second = first
  			first = array[i]
  		elif array[i]>second:
  			second = array[i]
  	res.append(first)
  	res.append(second)
  	return res