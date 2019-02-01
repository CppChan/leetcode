class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def maxheight(self, root):
		stack, maxheight= [],[0, None]
		self.preorder(root, stack, maxheight)
		return maxheight[1]

	def preorder(self, root, stack,maxheight):
		if not root:return
		stack.append(root)
		if len(stack)>maxheight[0]: maxheight[0], maxheight[1]=len(stack),stack[-1]
		elif len(stack)==maxheight[0]: maxheight[1]=stack[-1]
		self.preorder(root.left, stack, maxheight)
		self.preorder(root.right, stack, maxheight)
		stack.pop()


if __name__=="__main__":
    s = Solution()
    a =TreeNode(8)
    b =TreeNode(5)
    c =TreeNode(10)
    d =TreeNode(3)
    e = TreeNode(7)
    f = TreeNode(9)
    g = TreeNode(12)
    a.left, a.right= b,c
    b.left, b.right= d,e
    c.left, c.right =f,g
    e.left = TreeNode(6)
    print s.maxheight(a).val
