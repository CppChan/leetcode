class Solution(object):
  def longestConsecutive(self, root):
  	if not root: return 0
  	res = [0]
  	self.findpath(root, res)
  	return res[0]

  def findpath(self, root, res):
  	if not root: return 0
  	left = self.findpath(root.left, res)
  	right = self.findpath(root.right, res)
  	templong = 1
  	if root.left and root.left.val-1==root.val: templong = left+1
  	if root.right and root.right.val-1 == root.val and right+1>templong: templong = right+1
  	if templong>res[0]:res[0]= templong
  	return templong