from collections import deque
class Solution(object):
  def validTree(self, n, edges):
  	if len(edges)==0 and (n == 1 or n ==0):return True
  	elif len(edges)==0 :return False
  	isvisit, edge_dic, queue= [0]*n,{},deque([])
  	for i in range(len(edges)):
  		if edges[i][0] not in edge_dic: edge_dic[edges[i][0]]=[edges[i][1]]
  		else: edge_dic[edges[i][0]].append(edges[i][1])
  		if edges[i][1] not in edge_dic: edge_dic[edges[i][1]]=[edges[i][0]]
  		else: edge_dic[edges[i][1]].append(edges[i][0])
  	queue.append(edge_dic.items()[0][0])
  	isvisit[edge_dic.items()[0][0]]=1
  	while len(queue)>0:
  		node = queue.popleft()
  		if node not in edge_dic: continue
  		reach = edge_dic[node]
  		for i in range(len(reach)):
  			if isvisit[reach[i]]==1:return False
  			if isvisit[reach[i]]==0:
  				isvisit[reach[i]]=1
  				queue.append(reach[i])
  		isvisit[node]=2 #here is important, this point will not be visit again
  	for i in isvisit:
  		if i == 0:return False
  	return True

  # class Solution(object):
	#   def validTree(self, n, edges):
	# 	  if n == 1 and len(edges) == 0: return True
	# 	  dic = {}
	# 	  for i in edges:
	# 		  a, b = i[0], i[1]
	# 		  if not dic.has_key(a): dic[a] = []
	# 		  if not dic.has_key(b): dic[b] = []
	# 		  dic[a].append([a, b])
	# 		  dic[b].append([b, a])
	# 	  if len(dic) < n: return False
	# 	  level, pre = [0], set([0])
	# 	  while len(level) > 0:
	# 		  newlevel = []
	# 		  for i in level:
	# 			  if dic.has_key(i):  # corner!!! because may be i is the last node in one shuzhi
	# 				  son = dic[i]
	# 				  while len(son) > 0:  # cannot use for j in son, because len(son) is decreasing
	# 					  j = son[0]
	# 					  dic[j[1]].remove([j[1], j[0]])
	# 					  dic[i].remove([i, j[1]])
	# 					  if j[1] in pre: return False
	# 					  pre.add(j[1])
	# 					  newlevel.append(j[1])
	# 					  if len(dic[j[1]]) == 0: dic.__delitem__(j[1])
	# 					  if len(dic[j[0]]) == 0: dic.__delitem__(j[0])
	# 		  level = newlevel
	# 	  if len(dic) > 0: return False
	# 	  return True

if __name__ == "__main__":
    s = Solution()
    s.validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]])