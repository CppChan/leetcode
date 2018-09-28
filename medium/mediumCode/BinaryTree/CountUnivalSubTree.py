class Solution(object):
  def countUnivalSubtrees(self, root):
  	if not root: return 0
  	return self.findsub(root)[0]

  def findsub(self, root):
  	if not root: return (0, True)
  	left = self.findsub(root.left)
  	right = self.findsub(root.right)
  	if ((root.left and root.left.val == root.val and left[1]) or not root.left) and ((root.right and root.right.val == root.val and right[1]) or not root.right):
  		return (left[0]+right[0]+1, True)
  	else: return(left[0]+right[0], False)