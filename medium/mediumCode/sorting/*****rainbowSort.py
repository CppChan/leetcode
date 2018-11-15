class Solution(object):
#this is better than quick sort which is nlogk
  def rainbowSortIII(self, array, k):
  	if len(array)==0 or len(array)==1: return array
  	self.bowsort(array, 0, len(array)-1, 1,k)
  	return array

  def bowsort(self, array, left, right, i, j):
  	if i >= j: return
  	if left >= right: return
  	mid = (i+j)/2
  	orileft,oriright = left, right
  	while left<=right:
  		while left<=right and array[left]<=mid:#corner case!!!! make left side is all <=mid
  			left+=1
  		while right>=left and array[right]>mid:#corner case!!!! make right side is all >mid
  			right-=1
  		if left<right:
  			temp = array[left]
  			array[left]=array[right]
  			array[right]=temp
  			left+=1
  			right-=1
	#until here, left is always = right-1
  	self.bowsort(array, orileft, right, i, mid)
  	self.bowsort(array, left,oriright ,mid+1, j)#right side is all >mid


#general rainbow sort with three colors
class Solution2(object):
	def rainbowSort(self, array):
		"""
        input: int[] array
        return: int[]
        """
		# write your solution here
		if len(array) == 0:
			return []
		i = 0
		j = 0
		k = len(array) - 1
		while (j <= k):
			if (array[j] == -1):
				self.swap(array, i, j) # here, array[i], array[j] wont be 1, 1 must have been moved to last,
				# array[i] wont be -1, because when array[i]==-1, must i++, so array[i] must be 0
				i, j = i + 1, j + 1
			elif (array[j] == 0):
				j = j + 1
			elif (array[j] == 1):
				self.swap(array, j, k)
				k = k - 1
		return array

	def swap(self, array, a, b):
		temp = array[a]
		array[a] = array[b]
		array[b] = temp