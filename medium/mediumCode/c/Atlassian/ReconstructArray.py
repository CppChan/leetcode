class Solution(object):
	def reconstruct(self, n, m, totalCost):
		res = [0]
		for i in range(1, m+1-totalCost):
			self.dfs(i, n-1, m, totalCost,res)
		return res[0]

	def dfs(self, pre_max, n, m, totalCost, res):
		if totalCost<0:return
		if n==0:
			res[0]+=1
			return
		if n>totalCost:
			for i in range(1,pre_max+1):
				self.dfs(pre_max, n-1, m, totalCost,res)
		for i in range(pre_max+1, m+1-(totalCost-1)):
			self.dfs(i, n-1, m, totalCost-1,res)
s = Solution()
print s.reconstruct(4,3,2)