class Solution(object):
	def shortestpath(self, input):
		shortest = [[float('inf')]*len(input) for i in range(len(input))]
		for i in range(len(input)):
			self.dijkstra(i, input, shortest)
		return shortest

	def dijkstra(self, i, input, shortest):
		path = shortest[i]
		path[i], ingroup, newmember= 0,[False]*len(input), i
		ingroup[i] = True
		for k in range(len(input)-1):
			for out in range(len(input)):
				path[out] = min(input[newmember][out]+path[newmember], path[out])
			newshortest= float('inf')
			for j in range(len(input)):
				if not ingroup[j] and path[j]<newshortest:newshortest, newmember = path[j], j
			ingroup[newmember]=True


# graph pic in https://blog.csdn.net/fengchi863/article/details/80049681
s = Solution()
print s.shortestpath([[0,1,1,4,float('inf'),2,5,float('inf')],[1,0,float('inf'),float('inf'),float('inf'),2,float('inf'),4],[1,float('inf'),0,float('inf'),float('inf'),float('inf'),3,float('inf')],[4,float('inf'),float('inf'),0,1,float('inf'),float('inf'),float('inf')]
                ,[float('inf'),float('inf'),float('inf'),1,0,1,float('inf'),float('inf')],[2,2,float('inf'),float('inf'),1,0,float('inf'),float('inf')],
                [5,float('inf'),3,float('inf'),float('inf'),float('inf'),0,1],[float('inf'),4,float('inf'),float('inf'),float('inf'),float('inf'),1,0]])