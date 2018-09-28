class Solution(object):
  def diagonalSum(self, root):
  	dic = {}
  	if not root: return 0
  	self.bianli(root, dic, 1, 0)
  	res = []
  	for item in sorted(dic.iteritems(), key=lambda d: d[0]):
  		temp = 0
  		for i in range(len(item[1])):
  			temp+=item[1][i]
  		res.append(temp)
  	return res

  def bianli(self, root, dic, level, index):
  	if not root: return
  	if level-index not in dic:
  		dic[level-index] = []
  		dic[level-index].append(root.val)
  	elif level-index in dic:dic[level-index].append(root.val)
  	self.bianli(root.left, dic, level+1, index-1)
  	self.bianli(root.right, dic, level+1, index+1)