class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class solution(object):
    def smallestlowestCommonAncestor(self, root, p, q):
    	if not root:return None
    	smallest, hasfind= None,[False]
    	return self.find(root, p, q, hasfind, smallest)

    def find(self, root, p, q, hasfind, smallest):
    	if root in (None, p, q):return root
    	left, right = self.find(root.left, p, q,hasfind, smallest), self.find(root.right, p, q,hasfind, smallest)
    	if left and right:
    		hasfind[0], smallest= True, root
    		return smallest
    	else:
    		if hasfind[0]:
    			if left and left.val>root.val: smallest = root
    			elif right and right.val>root.val: smallest = root
    			return smallest
    		else:
    			if left:return left
    			else:return right

    def lowestCommonAncestor(self, root, p, q):#sososo efficient!!!!
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right #if left and not right return left; if right and not left return right
if __name__ == "__main__":
    s = solution()
    q = TreeNode(3)
    a = TreeNode(10)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(8)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    q.left = a
    print s.smallestlowestCommonAncestor(q, f, d).val
    print s.lowestCommonAncestor(q,f,d).val


