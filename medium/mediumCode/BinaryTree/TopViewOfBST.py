from collections import deque
class Solution(object):
  def topView(self, root):
  	res = []
  	if not root: return res
  	res.append(root.val)
  	queue = deque([])
  	queue.append((root,0))
  	mostleft, mostright = 0,0
  	levelnum = 1
  	while queue:
  		newlevel = 0
  		for i in range(levelnum):
  			temp = queue.popleft()
  			if temp[1]<mostleft:
  				res.insert(0, temp[0].val)
  				mostleft = temp[1]
  			if temp[1]>mostright:
  				res.append(temp[0].val)
  				mostright = temp[1]
  			if temp[0].left:
  				queue.append((temp[0].left,temp[1]-1))
  				newlevel+=1
  			if temp[0].right:
  				queue.append((temp[0].right, temp[1]+1))
  				newlevel+=1
  		levelnum = newlevel
  	return res