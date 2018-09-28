class Solution(object):
  def trimTree(self, root, k):
  	if not root: return None
  	if k == 0: return root
  	return self.dfs(root, k, 1)

  def dfs(self, root, k, level):
  	if not root:
  		return None
  	root.left = self.dfs(root.left, k, level+1)
  	root.right = self.dfs(root.right, k, level+1)
  	if not root.left and not root.right and level<k: return None
  	else: return root