class Solution(object):
  def combinations(self, number):
  	dic = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
  	number = list(str(number))
  	i = 0
  	while i<len(number):
  		if number[i]=='0' or number[i]=='1':
  			number.pop(i)
  			continue
  		number[i]=int(number[i])
  		i+=1
  	if len(number)==0:return []
  	res = []
  	self.dfs(number, res, 0,dic,"")
  	return res

  def dfs(self, number, res, i,dic,temp):
  	if i == len(number):
  		res.append(temp)
  		return
  	for j in range(len(dic[number[i]])):
  		self.dfs(number, res, i+1, dic, temp+dic[number[i]][j])