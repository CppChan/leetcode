class Solution(object):
  def updateHeap(self, array, index, ele):
  	pre,array[index] = array[index],ele
  	if len(array)==1:return array
  	if ele>pre:self.pushdown(array, index)
  	elif ele<pre:self.up(array,index)
  	return array

  def pushdown(self, array, i):
  	left, right = False, False
  	if 2*i+1<len(array) and array[2*i+1]<array[i]:left = True
  	if 2*i+2<len(array) and ((not left and array[2*i+2]<array[i]) or (left and array[2*i+2]<array[2*i+1])):right = True
  	if not left and not right:return
  	if not right:
  		array[i], array[2*i+1] = array[2*i+1], array[i]
  		self.pushdown(array, 2*i+1)
  	elif right:
  		array[i], array[2*i+2] = array[2*i+2], array[i]
  		self.pushdown(array, 2*i+2)
  	return

  def up(self, array, i):# pay attention corner case
  	if i == 0:return
  	if (i-1)/2>=0 and array[i]<array[(i-1)/2]:
  		array[i],array[(i-1)/2] = array[(i-1)/2],array[i]
  		self.up(array, (i-1)/2)
  	return