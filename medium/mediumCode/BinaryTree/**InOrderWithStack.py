class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# rule, if one node has add its left and right into the stack , then it must be pop from the stack
class Solution(object):
	def inorder(self, root):
		stack,res = [root],[]
		while len(stack)>0:
			while stack[-1].left:
				stack.append(stack[-1].left)
			while len(stack)>0 and not stack[-1].right:
				res.append(stack[-1].val)
				stack.pop()
			if len(stack)>0:
				temp = stack.pop()
				res.append(temp.val)
				stack.append(temp.right)

		return res


if __name__=="__main__":
    s=Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(8)
    e = TreeNode(5)
    f = TreeNode(6)
    k = TreeNode(10)
    q = TreeNode(11)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    e.left = k
    f.right = q
    print s.inorder(a)