class Solution(object):
	def zigzagLevelOrder(self, root):
		if not root: return []
		queue, res, fromright= [root], [[root.val]],True
		while len(queue)>0:
			nextlevel, nextval= [],[]
			for i in range(len(queue)-1, -1, -1):
				temp = queue[i]
				left, right = temp.left, temp.right
				if not fromright: left,right = right, left
				if right:
					nextlevel.append(right)
					nextval.append(right.val)
				if left:
					nextlevel.append(left)
					nextval.append(left.val)
			fromright = not fromright
			queue = nextlevel
			if len(nextval)>0: res.append(nextval)
		return res