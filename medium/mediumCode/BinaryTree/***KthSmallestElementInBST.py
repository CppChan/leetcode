class Solution(object):
  def kthSmallest(self, root, k):
  	order, res, begin = [k],[], [False]
  	self.findk(root, order,res, begin)
  	return res[0]

  def findk(self, root, order, res, begin):
  	if not root and not begin[0]: 
  		begin[0]=True
  		return 
  	if not root: return 
  	self.findk(root.left, order, res, begin)
  	if begin[0]:
  		if order[0]==1: res.append(root.val)
  		order[0]-=1
  	self.findk(root.right, order, res, begin)