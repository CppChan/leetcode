from collections import deque
class Solution(object):
  def isMinHeap(self, root):
  	if not root: return True
  	queue = deque([])
  	queue.append(root)
  	if self.dete(root): return self.ifcomplete(queue)
  	else: return False

  def dete(self,root):
  	if not root:return True
  	if not root.left and not root.right: return True
  	return self.dete(root.left) and self.dete(root.right) and (not root.left or root.left.val>=root.val) and (not root.right or root.right.val>=root.val)
  def ifcomplete(self, queue):
  	isdele = False
  	while len(queue)>0:
  		root = queue.popleft()
  		if root.left:
  			if isdele: return False
  			else: queue.append(root.left)
  		elif not root.left:isdele = True
  		if root.right:
  			if isdele: return False
  			else: queue.append(root.right)
  		elif not root.right:isdele = True
  	return True