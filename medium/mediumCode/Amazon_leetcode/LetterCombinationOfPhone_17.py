class Solution(object):
  def letterCombinations(self, digits):
  	dic = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
  	res = []
  	if len(digits)==0:return res
  	self.dfs(digits, dic, 0, res, "")
  	return res

  def dfs(self, digits, dic, i, res, temp):
  	if i>=len(digits):
  		res.append(temp)
  		return
  	letter = dic[int(digits[i])]
  	for j in range(len(letter)):
  		temp+=letter[j]
  		self.dfs(digits, dic, i+1, res, temp)
  		temp=temp[:len(temp)-1]