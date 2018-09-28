#find a range that equals to target

class Solution(object):
  def range(self, array, target):
  	if len(array)==0:return [-1,-1]
  	if len(array)==1:
  		if target == array[0]:return[0,0]
  		else: return [-1,-1]
  	i,j = 0, len(array)-1
  	while i<j:
  		mid = (i+j)/2
  		if array[mid]>=target: j= mid
  		else: i=mid+1
  	left,right = -1,-1
  	if array[i]==target:left = i
  	if left == -1: return[-1,-1]
  	i,j = 0, len(array)-1
  	while i<j-1:#this is not the same as previous one!!!!!!! because if array[i] and array[j] both == target, will dead loop
  		mid = (i+j)/2
  		if array[mid]<=target: i=mid
  		else: j= mid-1
  	if array[i]==target:right = i
  	if array[j]==target:right = j
  	return [left, right]


if __name__ == "__main__":
    s=Solution()
    s.range([5,5,5,5,5],5)