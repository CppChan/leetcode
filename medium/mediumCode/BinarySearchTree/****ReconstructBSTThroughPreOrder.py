class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
  def reconstruct(self, pre):
  	if len(pre)==0:return None
  	root = TreeNode(pre[0])
  	pre.pop(0)#!!!!!!cannot write pre = pre[1:len(pre)], because in the recursion then it will refer to a new object
  	self.construct(pre,root,None,None)
  	return root

  def construct(self, pre, root, parent1,parent2):
  	if len(pre)==0:return
  	if pre[0]<root.val:
  		if not parent1 or pre[0]>parent1:
  			root.left = TreeNode(pre[0])
  			pre.pop(0)
  			self.construct(pre, root.left, parent1,root.val)
  		else:return
  	if len(pre)==0:return#corner case to judge, if pre is over
  	if pre[0]>root.val:
  		if not parent2 or pre[0]<parent2:
  			root.right = TreeNode(pre[0])
  			pre.pop(0)
  			self.construct(pre, root.right, root.val, parent2)
  		else: return

if __name__ == "__main__":
    s = Solution()
    s.reconstruct([5, 3, 1, 4, 8, 11])