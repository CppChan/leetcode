from collections import deque
class Solution(object):
	def ifconnected(self, connection, a, b):
		if a<0 or a>=len(connection) or b<0 or b>len(connection) or a==b or connection[a][b]==1: return False
		queue, isvisit= deque([a]), set([a])
		while len(queue)>0:
			node = queue.pop()
			for i in range(len(connection)):
				if i in isvisit: continue
				if connection[node][i]==1:
					if i == b: return True
					queue.append(i)
					isvisit.add(i)
		return False


s = Solution()
print s.ifconnected([[0,0,1,0,1,0],[0,0,0,0,0,1],[1,0,0,0,0,0],[0,0,0,0,1,0],[1,0,0,1,0,0],[0,1,0,0,0,0]],2,4)