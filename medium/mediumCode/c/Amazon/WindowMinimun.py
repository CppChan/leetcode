from collections import deque
class Solution(object):
  def minWindow(self, input, k):
  	if len(input)==0:return []
  	if k==1:return input
  	index,res= deque([]),[]
  	for i in range(len(input)):
  		j = 0
  		while j<len(index):
  			if i-index[j]>=k: index.popleft()
  			else:break
  		while len(index)>0:
  			if input[index[-1]]>input[i]: index.pop()
  			else:break
  		index.append(i)
  		if index[-1]>=k-1:
  			res.append(input[index[0]])
  	return res

if __name__ == "__main__":
    s = Solution()
    print s.minWindow([4,2,12,11,5,3,6], 3)