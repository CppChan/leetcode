class Solution(object):
	def exist(self, root, target):
		if not root:
			return False
		elif self.findpath(root, target,0):
			return True
		else:
			return self.exist(root.left, target) or self.exist(root.right, target)

	def findpath(self, root, target, pre):
		if not root:
			return False
		else:
			if pre+root.val==target:
				return True
			else:
				return self.findpath(root.left, target, pre+root.val) or self.findpath(root.right, target, pre+root.val)
