class Solution(object):
  def search(self, array, target):
  	if len(array)==0: return -1
  	if len(array)==1:
  		if array[0]==target:return 0
  		else:return -1
  	i, j, mid =0, len(array)-1,0
  	while i<j-1:
  		mid = (i+j)/2
  		if array[mid]==target:return mid
  		if array[mid]>array[mid-1] and array[mid]>array[mid+1]:break
  		elif array[mid]>array[mid-1] and array[mid]<array[mid+1]:i=mid
  		elif array[mid]<array[mid-1] and array[mid]>array[mid+1]:j=mid
  	if array[i]>array[j]: mid = i
  	else: mid = j
  	i,j=0,mid
  	while i<j:
  		left =(i+j)/2
  		if array[left]==target:return left
  		elif array[left]>target:j=left-1
  		else:i=left+1
  	i,j=mid, len(array)-1
   	while i<j:
  		r =(i+j)/2
  		if array[r]==target:return r
  		elif array[r]>target:i=r+1
  		else:j=r-1
  	return -1