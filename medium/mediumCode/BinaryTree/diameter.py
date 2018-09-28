class Solution(object):
  def diameter(self, root):
  	if not root:
  		return 0
  	if not root.left:
  		return self.diameter(root.right)
  	elif not root.right:
  		return self.diameter(root.left)
  	res = [0]
  	self.findLongestTwo(root, res)
  	return res[0]

  def findLongestTwo(self, root, res):
  	if not root:
  		return 0
  	temp = self.findLongestTwo(root.left, res)+self.findLongestTwo(root.right, res)+1
  	if temp>res[0]:
  		res[0]=temp
  	return max(self.findLongestTwo(root.left,res),self.findLongestTwo(root.right,res))+1