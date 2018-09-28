class Solution(object):
  def verticalOrder(self, root):
  	dic = {}
  	res = []
  	if not root: return res
  	self.bianli(root, dic, 1, 0)
  	for item in sorted(dic.iteritems(), key=lambda d: d[0]):
  		temp = sorted(item[1], key = lambda x: x[0])
  		for i in range(len(temp)):
  			res.append(temp[i][1])
  	return res

  def bianli(self, root, dic, level, index):
  	if not root: return
  	if index not in dic:
  		dic[index] = []
  		dic[index].append((level, root.val))
  	elif index in dic:dic[index].append((level, root.val))
  	self.bianli(root.left, dic, level+1, index-1)
  	self.bianli(root.right, dic, level+1, index+1)
