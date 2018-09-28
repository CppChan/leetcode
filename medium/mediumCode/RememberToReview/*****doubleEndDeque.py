from collections import deque
class Solution(object):
  def maxWindows(self, array, k):
  	if len(array)==0:return array
  	k = min(len(array),k)
  	if k == 1:return array
  	res,index= [],deque([])
  	for i in range(len(array)):
  		while len(index)>0 and index[0]<i-k+1:
  			index.popleft()
  		while len(index)>0 and array[i]>array[index[-1]]:
  			index.pop()
  		index.append(i)
  		if i>=k-1:res.append(array[index[0]])
  	return res

if __name__=="__main__":
	s = deque([])
	s.append(2)
	s.appendleft(1)
	print s

#https://leetcode.com/problems/sliding-window-maximum/discuss/65884/Java-O(n)-solution-using-deque-with-explanation?page=2

#At each iteration, first delete the left most element that beyond the window,
# then begin at rightest side on the left of the array[I], delete elements that are smaller than array[I],
# finally maintain the deque at decreasing order, and the left most element is the maximum in  window