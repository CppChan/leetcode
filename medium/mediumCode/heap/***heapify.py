class Solution(object):
	# better version

	def heapify(self, array):
		for i in range(len(array) - 1, -1, -1):
			self.minsiftdown(array, len(array), i)
		return array

	def minsiftdown(self, array, n, i):
		left = 2 * i + 1
		right = 2 * i + 2
		minindex = i
		if left < n and array[i] > array[left]:
			minindex = left
		if right < n and array[minindex] > array[right]:
			minindex = right
		if minindex != i:
			array[i], array[minindex] = array[minindex], array[i]
			self.minsiftdown(array, n, minindex)

def heapify(self, array):# not good version
  	if len(array)==0 or len(array)==1: return array
  	i = (len(array)/2)-1
  	while i>0:
  		if ((i+1)*2-1>=len(array) or array[i]<array[(i+1)*2-1]) and ((i+1)*2>=len(array) or array[i]<array[(i+1)*2]):i-=1
  		else:
  			self.topdown(array, i)
  			i-=1
  	while ((i+1)*2-1<len(array) and array[i]>array[(i+1)*2-1]) or ((i+1)*2<len(array) and array[i]>array[(i+1)*2]):
  		pre = array[i]
  		self.topdown(array,i)
  		if (i+1)*2-1<len(array) and array[(i+1)*2-1]==pre: i = (i+1)*2-1
  		elif (i+1)*2<len(array) and array[(i+1)*2]==pre: i = (i+1)*2
  	return array

def topdown(self,array, i):
    if (i+1)*2-1<len(array) and array[i]>array[(i+1)*2-1] and (i+1)*2<len(array) and array[i]>array[(i+1)*2]:
		if array[(i+1)*2-1]<=array[(i+1)*2]:
			temp = array[(i+1)*2-1]
			array[(i+1)*2-1]= array[i]
			array[i]=temp
		else:
			temp = array[(i+1)*2]
			array[(i+1)*2]= array[i]
			array[i]=temp
    elif (i+1)*2-1<len(array) and array[i]>array[(i+1)*2-1]:
		temp = array[(i+1)*2-1]
		array[(i+1)*2-1]= array[i]
		array[i]=temp
    elif (i+1)*2<len(array) and array[i]>array[(i+1)*2]:
		temp = array[(i+1)*2]
		array[(i+1)*2]= array[i]
		array[i]=temp




if __name__ == "__main__":
    s= Solution()
    s.heapify([5,4,3,2,1,0])