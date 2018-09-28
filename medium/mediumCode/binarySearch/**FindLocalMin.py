class Solution(object):
  def localMinimum(self, array):
  	if len(array)==1: return 0
  	i, j = 0, len(array)-1
  	while i<j-1:
  		mid = (i+j)/2
  		if array[mid]<array[mid+1] and array[mid]< array[mid-1]:return mid
  		if array[mid]>=array[mid-1]: j = mid
  		elif array[mid]>=array[mid+1]:i = mid
  	if array[i]<array[j]:return i
  	else: return j