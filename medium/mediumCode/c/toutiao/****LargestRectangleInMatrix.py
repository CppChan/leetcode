# similar as largest rectangle in histogram
class Solution(object):
	def maximalRectangle(self, matrix):
		if len(matrix)==0:return 0
		res, height, stack= 0, [0]*(len(matrix[0])+1),[-1]
		for i in range(len(matrix)):
			stack = [-1]
			for j in range(len(matrix[0])):
				if matrix[i][j]=="1": height[j]+=1
				else: height[j]=0
			res = max(res,self.compute(height, stack))
		return res
	def compute(self,height, stack):
		res = 0
		for i in range(len(height)):
			while height[i]<height[stack[-1]]:
				h = height[stack.pop()]
				w = i-1-stack[-1]
				res = max(res, h*w)
			stack.append(i)
		return res