class Solution(object):
  def depth(self, forest):
  	dic = {}
  	res = -1
  	if len(forest)==1:return 1
  	for i in range(len(forest)):
  		if not dic.has_key(i):
  			temp = self.dfs(forest, i, dic)
  			if temp==-1:return -1
  			if temp>res:res = temp
  	return res

  def dfs(self, forest, i, dic):
  	if forest[i]==-1:
  		dic[i]=1
  		return 1
  	if dic.has_key(forest[i]):
  		if dic[forest[i]]==-1: dic[i]=-1
  		else:dic[i]=1+dic[forest[i]]
  	else:
  		dic[i]=-1
  		height = self.dfs(forest, forest[i], dic)
  		if height==-1:dic[i]=-1
  		else:dic[i]=1+height
  	return dic[i]