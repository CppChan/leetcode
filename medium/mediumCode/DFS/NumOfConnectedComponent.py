class Solution(object):
  def countComponents(self, n, edges):
  	if n == 0: return 0
  	if n ==1:return 1
  	dic = {}
  	for i in range(n):
  		dic[i]=[]
  	for i in range(len(edges)):
  		dic[edges[i][0]].append(edges[i][1])
  		dic[edges[i][1]].append(edges[i][0])
  	res = [0]
  	for i in range(n):
  		if dic.has_key(i):
			self.dfs(dic, res, i)
			res[0]+=1
	return res[0]

  def dfs(self, dic, res, now):
  	if len(dic[now])==0:
  		dic.__delitem__(now)
  		return
  	i=0
  	while len(dic[now])>0:
  		temp = dic[now][0]
  		dic[now].pop(0)
  		dic[temp].remove(now)
  		if len(dic[now])==0: dic.__delitem__(now)
  		if len(dic[temp])==0: dic.__delitem__(temp)
  		if dic.has_key(temp):self.dfs(dic, res, temp)
  		if not dic.has_key(now):break
  	return