class Solution(object):
  def findLocalMax(self, array):
  	if len(array)==1: return 0
  	i, j = 0, len(array)-1
  	while i<j-1:# why use i<j-1, this can avoid that med = 0 or med = len(s)-1
  		mid = (i+j)/2
  		if array[mid]>array[mid+1] and array[mid]> array[mid-1]:return mid
  		if array[mid]<array[mid-1]: j = mid-1
  		elif array[mid]<array[mid+1]:i = mid+1
  	if array[i]>array[j]:return i
  	else: return j


# class Solution(object):#find local max
#   def findLocalMax(self, input):#any
#   	i,j = 0, len(input)-1
#   	if len(input)==1:return input[0]
#   	while i<j:
#   		med = (i+j)/2
#   		if (med-1>=0 and med+1<len(input) and input[med]>input[med-1] and input[med]>input[med+1])or (med == 0 and input[0]>input[1]) or (med==len(input)-1 and input[med]>input[med-1]):return med
#   		if med+1<len(input) and input[med]<input[med+1]:i = med+1
#   		elif med-1>=0 and input[med]<input[med-1]: j = med-1
#   	if i == j and (i==0 or i==len(input)-1 or (input[i]>input[i-1] and input[i]>input[i+1])):return i


if __name__=="__main__":
	s=Solution()
	print s.findLocalMax([1,2,3,4,5,5,6,2,3])