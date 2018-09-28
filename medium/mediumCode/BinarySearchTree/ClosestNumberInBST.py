class Solution(object):
  def closestKValues(self, root, target, k):
  	if k <=0:return []
  	nodes, closest= [],[float('inf')]
  	self.inorder(root, nodes, closest, target)
  	if k>=len(nodes): return nodes
  	left,right,k, res= nodes.index(closest[0])-1,nodes.index(closest[0])+1,k-1,[closest[0]]
  	while k>0:
  		if left<0:
  			res.append(nodes[right])
  			right,k=right+1,k-1
  		elif right>=len(nodes):
  			res.insert(0,nodes[left])
  			left,k=left-1,k-1
  		else:
  			if abs(nodes[left]-target)<=abs(nodes[right]-target):
  				res.insert(0, nodes[left])
  				left,k=left-1,k-1
  			else:
  				res.append(nodes[right])
  				right,k=right+1,k-1
  	return res

  def inorder(self, root, nodes, closest, target):
  	if not root: return
  	self.inorder(root.left, nodes,closest, target)
  	nodes.append(root.val)
  	if abs(root.val-target)<abs(closest[0]-target): closest[0]=root.val
  	self.inorder(root.right,nodes,closest, target)