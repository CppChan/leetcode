class Solution(object):
  def reverse(self, input):
  	if not input or len(input)<1:return ""
  	input = list(input)
  	i,j = 0, len(input)-1
  	while i<j:
  		while i<j and i<len(input)-1 and input[i] not in ["a","e","i","o","u"]:
  			i+=1
  		while j>i and j>0 and input[j] not in ["a","e","i","o","u"]:
  			j-=1
  		if i>=j: break
  		input[i],input[j]=input[j],input[i]
  		i+=1
  		j-=1
  	return "".join(input)