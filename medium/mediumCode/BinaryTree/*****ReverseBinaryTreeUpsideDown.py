import copy
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  newroot = None
  temproot = None#use global variable
  def reverse(self, root):
  	if not root:
  		return root
  	self.newroot = TreeNode(0)
  	self.newroot.left = copy.deepcopy(root)#!!!deepcopy!!!!!!!
  	self.temproot = self.newroot.left
  	self.inorder(root, False)
  	return self.newroot.left

  def inorder(self, root, isright):
  	if not root and isright:
  		self.temproot.right = None
  		self.temproot = self.temproot.left
  		isright = False
  		return
  	if not root.left and not root.right and not isright:
  		self.temproot.val = root.val
  		return
  	if isright and root:
  		if not self.temproot.right:
  			self.temproot.right = TreeNode(root.val)
  		else:
  			self.temproot.right.val = root.val
  		self.temproot = self.temproot.left
  		isright = False
  		return
  	self.inorder(root.left, isright)
  	self.temproot.left.val= root.val
  	isright = True
  	self.inorder(root.right, isright)


if __name__ == "__main__":
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.left.left = TreeNode(4)
    a.left.right = TreeNode(5)
    s = Solution()
    print s.reverse(a)


class solution(object):
  def reverse(self, root):#wrong code, try best not to use recursion when dealing with linkedlist, unless use global variable
  	newroot = TreeNode(0)
  	temproot = newroot
  	temproot = temproot.left
  	self.inorder(root, temproot, False)
  	return newroot.left

  def inorder(self, root, temproot, isright):
  	if not root and isright:
  		temproot.right = None
  		temproot = temproot.left
  		isright = False
  		return temproot
  	if not root.left and not root.right and not isright:
  		temproot = TreeNode(root.val)
  		return temproot
  	if isright and root:
  		temproot.right = TreeNode(root.val)
  		temproot = temproot.left
  		isright = False
  		return temproot
  	temproot = self.inorder(root.left, temproot,isright)
  	temproot.left= TreeNode(root.val)
  	isright = True
  	temproot = self.inorder(root.right, temproot,isright)
  	return temproot

