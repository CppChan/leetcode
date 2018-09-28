class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  accu = 0
  def greaterSum(self, root):
  	if not root:return None
  	if (not root.left and not root.right): return TreeNode(0)
  	newroot = self.buildRoot(root)
  	self.inorder(newroot, root)
  	return newroot

  def inorder(self, newroot, root):
  	if not root and not newroot:
  		return
  	self.inorder(newroot.right, root.right)
  	newroot.val = self.accu
  	self.accu+=root.val
  	self.inorder(newroot.left, root.left)

  def buildRoot(self,root):
  	if not root:return None
  	newroot = TreeNode(0)
  	newroot.left = self.buildRoot(root.left)
  	newroot.right = self.buildRoot(root.right)
  	return newroot


if __name__ == "__main__":

    s = Solution()
    # a = TreeNode(3)
    # b = TreeNode(2)
    # c = TreeNode(1)
    # a.left = b
    # b.left = c
    # s.greaterSum()