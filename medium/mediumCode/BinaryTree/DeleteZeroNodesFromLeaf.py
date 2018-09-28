class Solution(object):
  def delete(self, root):
  	if not root: return None
  	root = self.dele(root)
  	return root

  def dele(self, root):
  	if not root: return None
  	if root.val == 0 and not root.left and not root.right:
  		return None
  	root.left = self.dele(root.left)
  	root.right = self.dele(root.right)
  	if root.val == 0 and not root.left and not root.right:
  		return None
  	else: return root