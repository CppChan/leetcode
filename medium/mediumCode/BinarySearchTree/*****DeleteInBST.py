class Solution(object):
  def delete(self, root, key):
  	self.findNode(root,key)
  	return root

  def findNode(self, root, key):
  	if not root:return
  	elif root.val == key:
  		if not root.right:return root.left
  		elif not root.left: return root.right #!!!!!!!!this is important, corner case,no extra discussion
  		else:
  			tuple = self.goright(root.right)
  			root.right, root.val= tuple[1],tuple[0]
  			return root
  	else:
  		if root.val>key: root.left = self.findNode(root.left,key)
  		else:root.right = self.findNode(root.right,key)
  		return root

  def goright(self, node):
  	if not node.left: return(node.val,node.right)
  	tuple = self.goright(node.left)
  	node.left = tuple[1]
  	return(tuple[0],node)