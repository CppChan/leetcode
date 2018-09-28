class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
		self.total_left = 0

class Solution(object):
    def compute(self, root):
	    if not root:
		    return 0
	    else:
		    root.total_left = self.compute(root.left)
		    return root.total_left + self.compute(root.right)+1

if __name__ == "__main__":
    s = Solution()
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(2)
    d = TreeNode(6)
    e = TreeNode(4)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    s.compute(a)
    print a.total_left, b.total_left, c.total_left, d.total_left, e.total_left