class Solution(object):
  def validTree(self, n, edges):
  	if n == 1 and len(edges)==0:return True
  	dic = {}
  	for i in edges:
  		a, b = i[0],i[1]
  		if not dic.has_key(a): dic[a]=[]
  		if not dic.has_key(b): dic[b]=[]
  		dic[a].append([a,b])
  		dic[b].append([b,a])
  	if len(dic)<n: return False
  	level, pre= [0], set([0])
  	while len(level)>0:
  		newlevel = []
  		for i in level:
  			if dic.has_key(i):# corner!!! because may be i is the last node in one shuzhi
	  			son = dic[i]
	  			while len(son)>0: #cannot use for j in son, because len(son) is decreasing
	  				j = son[0]
	  				dic[j[1]].remove([j[1], j[0]])
	  				dic[i].remove([i, j[1]])
	  				if j[1] in pre:return False
	  				pre.add(j[1])
	  				newlevel.append(j[1])
	  				if len(dic[j[1]])==0: dic.__delitem__(j[1])
	  				if len(dic[j[0]])==0: dic.__delitem__(j[0])
  		level = newlevel
  	if len(dic)>0:return False
  	return True

if __name__ == "__main__":
    s = Solution()
    s.validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]])