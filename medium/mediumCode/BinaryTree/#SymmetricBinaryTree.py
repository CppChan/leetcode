class Solution(object):
  def isSymmetric(self, root):
  	if not root:return True
  	return self.check(root.left, root.right)

  def check(self, left, right):
  	if not left and not right:return True
  	if (not left and right) or (left and not right):return False
  	return left.val == right.val and self.check(left.right, right.left) and self.check(left.left, right.right)
