class Solution(object):
  def dedup(self, array):
  	if len(array)<3:return array
  	i = 2
  	while i <len(array):
        # should use while but not for loop see below
  		if array[i]==array[i-1] and array[i]==array[i-2]:
  			array.pop(i)
  			continue
  		i+=1
  	return array



class Solution(object):
  def dedup(self, array):
  	if len(array)<3:return array
  	for i in range(2, len(array)):#here is corner case, when del array[2], then i = 1, will not go into the loop
  		if array[i]==array[i-1] and array[i]==array[i-2]:
  			array.pop(i)
  			i-=1
  	return array