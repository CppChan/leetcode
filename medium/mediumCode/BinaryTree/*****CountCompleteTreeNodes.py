class Solution(object):
  def find(self, root):
  	if not root:return 0
  	height = self.height(root)
  	return self.findheight(root, height)

  def findheight(self, root, height):
  	if not root.left and not root.right: return 1
  	if self.height(root.right)<height-1: return self.findheight(root.left, height-1)+2**(n-2)
  	else: return self.findheight(root.right, height-1)+2**(n-1)+1

  def height(self, root):
  	if not root: return 0
  	return 1+self.height(root.left)