class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def treeToDoublyList(self, root):
    	if not root:return None
    	dummy = TreeNode(0)
    	last = self.inorder(root, dummy)
    	dummy.right.left = last
    	last.right = dummy.right
    	return dummy.right

    def inorder(self, root, pre):
   		if not root: return pre
   		prenode = self.inorder(root.left, pre)
   		root.left = prenode
   		prenode.right = root
   		return self.inorder(root.right, root)

if __name__ == "__main__":
    s = Solution()
    a = TreeNode(4)
    b = TreeNode(2)
    c = TreeNode(7)
    d = TreeNode(1)
    e = TreeNode(3)
    f = TreeNode(5)
    a.left = b
    a.right = c
    b.left, b.right = d, e
    c.left = f
    s.treeToDoublyList(a)