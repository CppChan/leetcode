class Solution(object):
  def longest(self, input):
  	if len(input)==0:return 0
  	dic = {input[0]:0}
  	if len(input)==1:return 1
  	i,j,res= 0,1,1
  	while i<j and i<len(input) and j<len(input):
  		if not dic.has_key(input[j]):
  			dic[input[j]]=j
  		else:
  			pre = dic[input[j]]
  			for k in range(i, pre+1):
  				dic.__delitem__(input[k])
  			dic[input[j]]=j
  			i = pre+1
  		res = max(res, j-i+1)
  		j+=1
  	return res

#maintain two pointers