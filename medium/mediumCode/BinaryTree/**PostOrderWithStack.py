from collections import defaultdict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def postorder(self, root):
		stack,res, dic= [root],[],defaultdict(lambda:0)
		while len(stack)>0:
			while stack[-1].left:
				stack.append(stack[-1].left)
			while len(stack)>0 and (not stack[-1].right or dic[stack[-1]]==1):
				res.append(stack[-1].val)
				stack.pop()
			if len(stack)>0:
				dic[stack[-1]]=1 # need to record that this node has been on the top of stack for once, means has goleft, now goright
				stack.append(stack[-1].right)
		return res

	def goleft(self, stack):
		newnode = stack[-1].left
		stack.append(newnode)

if __name__=="__main__":
    s=Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(8)
    e = TreeNode(5)
    f = TreeNode(6)
    # k = TreeNode(10)
    # q = TreeNode(11)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    # e.left = k
    # f.right = q
    print s.postorder(a)