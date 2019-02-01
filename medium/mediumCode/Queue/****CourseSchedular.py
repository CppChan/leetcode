from collections import deque
class Solution(object):
    def findOrder(self, n, input):
    	prer, res = [0]*n,[]
    	for i in range(len(input)):
    		prer[input[i][0]]+=1
    	queue = deque([])
    	for i in range(len(prer)):
    		if prer[i]==0:queue.append(i)
    	while len(queue)>0:
    		cur = queue.popleft()
    		res.append(cur)
    		for i in range(len(input)):
    			if input[i][1]==cur:
    				prer[input[i][0]]-=1
    				if prer[input[i][0]]==0: queue.append(input[i][0])
    	if len(res)==n:return res
    	return []