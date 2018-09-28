import heapq

class Solution(object):
  def maxPathSum1(self, root):#leaf node to leaf node
  	res = [-2147483648]
  	self.findLongestTwo(root, res)
  	return res[0]

  def findLongestTwo(self, root, res):
  	if not root:
  		return None
  	else:
  		if not self.findLongestTwo(root.left, res) and not self.findLongestTwo(root.right, res):
  			return [root.val]
  		else:
  			newtuple=[]
  			tuple1 = self.findLongestTwo(root.left, res)
  			tuple2 = self.findLongestTwo(root.right,res)
  			if tuple1:
  				newtuple.append(max(tuple1[:])+root.val)
  			if tuple2:
  				newtuple.append(max(tuple2[:])+root.val)
  			if len(newtuple)>=2:
  				if newtuple[0]+newtuple[1]-root.val>res[0]:
  					res[0]= newtuple[0]+newtuple[1]-root.val
  			return newtuple

	def maxPathSum2(self, root):#any node
		res = [-float('inf')]
		self.findMax(root, res)
		return res[0]

	def findMax(self, root, res):
		if not root:
			return 0
		else:
			returnval = 0
			rootVal = 0
			left = self.findMax(root.left, res)
			right = self.findMax(root.right, res)
			if left < 0 and right < 0:
				rootVal = root.val
				returnval = root.val
			else:
				rootVal = max(root.val + max(left, right), root.val + left + right)
				returnval = root.val + max(left, right)
			if rootVal > res[0]:
				res[0] = rootVal
			return returnval

	def maxPathSum3(self, root):#path belong to a certain root to leaf node
		res = [-float('inf')]
		self.findMax(root, res)
		return res[0]

	def findMax(self, root, res):
		if not root:
			return 0
		else:
			rootVal = 0
			left = self.findMax(root.left, res)
			right = self.findMax(root.right, res)
			if left < 0 and right < 0:
				rootVal = root.val
			else:
				rootVal = root.val + max(left, right)
			if rootVal > res[0]:
				res[0] = rootVal
			return rootVal


if __name__ =="__main__":
    list = [1,2,3,3]
    print max(list[0:2])