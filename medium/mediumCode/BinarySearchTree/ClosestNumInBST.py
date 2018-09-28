class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class tuple(object):
	def __init__(self):
		self.val = 0

class Solution(object):
	def closest(self, root, target):
		res = tuple
		min = float('inf')
		self.findclosest(root, target, min, res)
		return res.val

	def findclosest(self, root, target, min, res):
		if abs(root.val-target)<min:
			res.val = root.val
			min = abs(root.val-target)
			if min == 0:
				return
		if target<root.val and root.left:
			self.findclosest(root.left, target, min, res)
		elif target>root.val and root.right:
			self.findclosest(root.right, target, min, res)