class Solution(object):
  def countArray(self, array):
  	if len(array)==0: return []
  	sortarray = sorted(array)
  	res = [0]*len(array)
  	for i in range(len(array)):
  		index = self.find(sortarray, array[i])
  		res[i]=index
  		sortarray.pop(index)
  	return res

  def find(self, array, item):
  	i,j=0,len(array)-1
  	while i<j:
  		mid = (i+j)/2
  		if array[mid]>=item:j = mid
  		if array[mid]<item: i = mid+1
  	return i