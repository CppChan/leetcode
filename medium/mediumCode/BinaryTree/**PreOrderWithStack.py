class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def preorder(self, root):
		stack,res = [root],[root.val]
		while len(stack)>0:
			while stack[-1].left: # goleft
				newnode = stack[-1].left
				stack.append(newnode)
				res.append(newnode.val)
			while len(stack)>0 and not stack[-1].right: #if a node dont have right, it wont be use again, pop it
				stack.pop()
			if len(stack)>0:
				temp = stack.pop()# temp must be hava a right node
				stack.append(temp.right)
				res.append(temp.right.val)
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
    print s.preorder(a)

