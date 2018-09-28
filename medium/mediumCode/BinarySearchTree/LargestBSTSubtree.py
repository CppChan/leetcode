class Solution(object):
  def largestBSTSubtree(self, root):
  	if not root: return 0
  	return self.findBST(root)[0]

  def findBST(self, root):
  	if not root:return None
  	elif not root.left and not root.right:
  		return (1, (root.val,root.val), True)
  	one = self.findBST(root.left)
  	two = self.findBST(root.right)
  	if (one and two) and(one[2] and two[2]) and (one[1][1]<root.val and two[1][0]>root.val):
  		return (one[0]+two[0]+1,(one[1][0], two[1][1]), True)
  	else:
  		if not one: return (two[0], two[1], False)
  		elif not two:return (one[0], one[1], False)
  		elif one[0]>=two[0]: return (one[0], one[1], False)
  		else:return (two[0], two[1], False)