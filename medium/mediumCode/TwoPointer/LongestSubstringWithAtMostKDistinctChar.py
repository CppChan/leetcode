class Solution(object):
  def lengthOfLongestSubstringTwoDistinct(self, input,k):
  	if len(input)<k: return 0
  	dic,i,j, res= {},0,0,0
  	while i <len(input) and j<len(input):
  		if not dic.has_key(input[j]): dic[input[j]]=1
  		else: dic[input[j]]+=1
  		j+=1
  		while len(dic)>k:
  			dic[input[i]]-=1
  			if dic[input[i]]==0: dic.__delitem__(input[i])
  			i+=1
  		res = max(res, j-i)
  	return res