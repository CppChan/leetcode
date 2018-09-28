class Solution(object):
  def flatten(self, root):
  	if not root: return root
  	root = self.flat(root,None)
  	return root

  def flat(self, root, pre):
  	if not root: return pre
  	right = self.flat(root.right, pre)
  	left = self.flat(root.left, right)
  	root.right = left
  	root.left = None
  	return root