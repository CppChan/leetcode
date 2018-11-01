class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object): # not promise to in the tree
  def lowestcommon2(self, root, one, two):
  	if not root: return False
  	found = [0,0]
  	parent = self.findnode(root, one, two, found)
  	if found[0] and found[1]:return parent
  	return None
  def findnode(self, root, one, two, found):
  	if not root:return None
  	if root==one: found[0]=1
  	if root == two:found[1]=1
  	left = self.findnode(root.left, one, two, found)
  	right = self.findnode(root.right, one, two, found)
  	if left and right: return root
  	if root==one or root==two:return root
  	if left:return left
  	else: return right


def lowestCommonAncestor(self, root, p, q):  # promise to in the tree, sososo efficient!!!!
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(kid, p, q)
                    for kid in (root.left, root.right))
    return root if left and right else left or right  # if left and not right return left; if right and not left return right


if __name__ == "__main__":
    s = Solution()
    q = TreeNode(10)
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(8)
    e = TreeNode(5)
    f = TreeNode(6)
    q.left = a
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    print s.lowestcommon2(q, f,f).val

