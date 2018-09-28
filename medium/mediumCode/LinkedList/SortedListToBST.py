class Solution(object):
  overhead = None
  def sortedListToBST(self, head):
  	size = 0
  	newhead = head
  	while newhead:
  		size+=1
  		newhead = newhead.next
  	root = self.buildTree(size)
  	self.overhead = head
  	self.inorder(root)
  	return root

  def buildTree(self, size):
  	if size == 0: return None
  	root = TreeNode(0)
  	if size%2 == 0:
  		root.left = self.buildTree(size/2-1)
  		root.right = self.buildTree((size/2))
  	else:
  		root.left = self.buildTree(size/2)
  		root.right = self.buildTree(size/2)
  	return root

  def inorder(self, root):
  	if not root:
  		return
  	self.inorder(root.left)
  	root.val = self.overhead.val
  	self.overhead = self.overhead.next
  	self.inorder(root.right)