class Solution(object):
  def generatePalindromes(self, input):
  	if len(input)==0:return []
  	dic,list= {},[]
  	for i in range(len(input)):
  		if not dic.has_key(input[i]):
  			dic[input[i]]=1
  			list.append(input[i])
  		else:
  			dic[input[i]]+=1
  			if dic[input[i]]%2==1: list.append(input[i])
  			else: list.remove(input[i])
  	if len(list)>1:return []
  	res,final= [],[]
  	if len(list)==1:
  		res.append(list[0])
  		dic[list[0]]-=1# cannot delete the key, because may be it has 3, 5, 7 elements
  	self.dfs(final,res, dic, len(input))
  	return final

  def dfs(self, final, res, dic, length):
  	if len(res)==length:
  		final.append("".join(res[:]))
  		return
  	for item in dic.iteritems():
  		if dic[item[0]]>0:
  			res.insert(0, item[0])
  			res.append(item[0])
  			dic[item[0]]-=2
  			self.dfs(final, res, dic, length)
  			dic[item[0]]+=2
  			res.pop(0)
  			res.pop(len(res)-1)
