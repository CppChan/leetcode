import datetime
class Solution(object):
	def solution(self,D, A):
		res,ancestor = [0]*len(A),0
		for i in range(len(A)):
			ancestor = i
			for j in range(D):
				ancestor = A[ancestor]
				if ancestor == -1: break
			res[i]=ancestor
		return res

	def solution2(self, D, A):
		dic, res= {},[0]*len(A)
		for i in range(len(A)):
			if A[i] != -1 and A[i] not in dic: dic[A[i]]=[i]
			elif A[i]!= -1: dic[A[i]].append(i)
		self.dfs(dic, [0], res, D)
		return res

	def dfs(self, dic, stack, res, D):
		if len(stack)<D+1: res[stack[-1]]=-1
		else: res[stack[-1]]= stack[-(D+1)]
		if stack[-1] in dic:
			sons = dic[stack[-1]]
			for son in sons:
				stack.append(son)
				self.dfs(dic, stack, res, D)
				stack.pop()

	def solution3(self, D, A):
		dp = [[0] * len(A) for i in range(D)]
		for i in range(D):
			for j in range(len(A)):
				if i == 0:dp[i][j] = A[j]
				else:
					if dp[i-1][j]==-1: dp[i][j]=-1
					else: dp[i][j] = dp[i - 1][A[j]]
		return dp[D - 1]

if __name__=="__main__":
	s = Solution()
	# starttime = datetime.datetime.now()
	# print s.solution(2,[-1,0,0,0,2,1,2,4,4,7])
	# print s.solution(3,[-1,0,0,0,2,1,2,4,4,7])
	# print s.solution(3,[-1,0,1,2,3,4])
	# print s.solution(1,[-1,0,1,2,3,4])
	# print s.solution(4,[-1,0,0,0,2,1,2,4,4,7])
	# print s.solution(2,[-1,0,1,2,1])
	# print s.solution(1,[-1,0])
	# print s.solution(1,[-1])
	# print s.solution(3,[-1,5,1,6,0,0,0,1])
	# print s.solution(2,[-1,5,1,6,0,0,0,1])
	# endtime = datetime.datetime.now()
	# print (endtime - starttime)

	# print s.solution(3,[-1,0,4,2,1])
	starttime = datetime.datetime.now()
	print s.solution2(3,[-1,0,4,2,1])
	print s.solution2(2,[-1,0,0,0,2,1,2,4,4,7])
	print s.solution2(3,[-1,0,0,0,2,1,2,4,4,7])
	print s.solution2(3,[-1,0,1,2,3,4])
	print s.solution2(1,[-1,0,1,2,3,4])
	print s.solution2(4,[-1,0,0,0,2,1,2,4,4,7])
	print s.solution2(2,[-1,0,1,2,1])
	print s.solution2(1,[-1,0])
	print s.solution2(1,[-1])
	print s.solution2(3,[-1,5,1,6,0,0,0,1])
	print s.solution2(2,[-1,5,1,6,0,0,0,1])
	endtime = datetime.datetime.now()
	print (endtime - starttime)