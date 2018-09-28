class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
  def distance(self, root, k1, k2):
  	if root == k1:return self.findnode(root, k2,0)
  	if root == k2: return self.findnode(root, k1,0)
  	return self.findcommon(root, k1, k2)[0]

  def findnode(self, root, k,depth):
  	if root == k: return depth
  	if not root: return 0
  	left = self.findnode(root.left, k, depth+1)
  	right = self.findnode(root.right, k, depth+1)
  	if left == 0: return right
  	else: return left

  def findcommon(self,root, k1, k2):
  	if not root:return (0, False)
  	if root == k1 or root == k2: return (0, True)
  	left = self.findcommon(root.left, k1, k2)
  	right = self.findcommon(root.right, k1, k2)
  	if left[1] and right[1]: return(left[0]+right[0]+2, False)
  	if left[1]: return(left[0]+1, True)
  	if right[1]: return(right[0]+1, True)
  	if not left[1] and not right[1]:
  		if left[0]>0:return (left[0], False)
  		if right[0]>0: return (right[0], False)
  	return(0, False)


if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    # b = TreeNode(2)
    c = TreeNode(3)
    # d = TreeNode(4)
    # e = TreeNode(5)
    # f = TreeNode(6)
    # g = TreeNode(7)
    # a.left = b
    a.right = c
    # b.left = d
    # b.right = e
    # c.left = f
    # c.right = g
    print s.distance(a, a, c)
