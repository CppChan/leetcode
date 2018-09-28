class Solution(object):
  def reorder(self, array):
  	if len(array)<4:return array
  	increase,i= (len(array)/2),0
  	while i<len(array) and increase>0:
  		temp = array[i+increase]
  		array.pop(i+increase)
		array.insert(i+1, temp)
		i+=2
		increase-=1
	return array
