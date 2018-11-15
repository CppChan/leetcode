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


class Solution2(object):
	ancestor, firstone, found= None, None, False
	def lowestCommonAncestor(self, root, p,q):
		self.find(root,p,q)
		if self.found:return self.ancestor #found means found two node
		return None

	def find(self, root, p, q):
		if not root or self.found:return
		self.find(root.left, p, q)
		self.check(root, p, q)#after going left, may be need to update ancestor
		self.find(root.right, p, q)
		self.check(root, p, q)

	def check(self, root, p, q): # check used to update ancestor(upgrade the ancestor to a parent node) or set the ancestor == firstnode
		if self.found:return #if found, dont need to check
		if not self.ancestor: # have not found anyone node
			if root == p:
				self.ancestor = p
				if not self.firstone:self.firstone = p
				if p==q:self.found = True
			if root == q:
				self.ancestor = q
				if not self.firstone:self.firstone = q
		else:
			if root.left==self.ancestor or root.right==self.ancestor: #have just found one node, the other is not in this track, need to update ancestor
				self.ancestor = root
			if (root == p or root==q) and root!=self.firstone: #found the second node, use root!=self.firstone, because one root node will be checked twice
				self.found = True


if __name__ == "__main__":
    s = Solution2()
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
    print s.lowestCommonAncestor(q, d, e).val

