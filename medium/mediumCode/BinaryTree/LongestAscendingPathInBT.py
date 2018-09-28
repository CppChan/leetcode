class Solution(object):
  def longest(self, root):
  	if not root: return 0
  	return self.findpath(root)[1]

  def findpath(self, root):
  	if not root: return (0,0)
  	left = self.findpath(root.left)
  	right = self.findpath(root.right)
  	lefttemp, righttemp = 0,0
  	if (not root.left) or (root.left and root.val<root.left.val):
  		lefttemp = left[0]+1
  	if(not root.right) or (root.right and root.val<root.right.val):
  		righttemp = right[0]+1
  	return (max(lefttemp, righttemp), max(left[1], right[1], max(lefttemp, righttemp)))
  	a  = '2'
	a.