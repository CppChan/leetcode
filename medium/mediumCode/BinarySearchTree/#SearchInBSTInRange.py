class Solution(object):
  def getRange(self, root, min, max):
  	res = []
  	self.binary(root, min, max, res)
  	return sorted(res)

  def binary(self, root, min, max, res):
  	if not root:return
  	if root.val<=max and root.val>=min: res.append(root.val)
  	if root.val>min:self.binary(root.left, min, max, res)
  	if root.val<max:self.binary(root.right, min, max, res)