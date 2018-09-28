class Solution(object):
  def missing(self, array):
  	if len(array)==0:return 1
  	i,j = 0, len(array)-1
  	while i<j-1:
  		k = (i+j)/2
  		if array[k]<=k+1: i = k
  		elif array[k]>k+1:j = k
  	if i == 0 and array[0]>1: return 1#corner!!!!
  	if j == len(array)-1 and array[j]==len(array):return array[j]+1#corner!!!!
  	return j+1