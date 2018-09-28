class Solution(object):
  def missing(self, array):
  	list = set([])
  	if len(array)==0: return 1
  	for i in range(len(array)):
  		if array[i] in list:
  			list.remove(array[i])
  		else:
  			if len(array)+2-array[i] != array[i]:
  				list.add(len(array)+2-array[i])
  	if len(list)==0:
  		return (len(array)+2)/2
  	else: return list.pop()