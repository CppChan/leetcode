class Solution(object):
	def firstOccur(self, input, target):
		if len(input)==0:return -1
		i,j=0,len(input)-1
		while i<j-1:
			mid = (i+j)/2
			if input[mid]<target: i = mid+1
			if input[mid]>=target: j=mid
		if input[i]==target:return i
		elif input[j]==target:return j
		return -1