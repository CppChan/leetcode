class Solution(object):
  def firstMissingPositive(self, input):
  	if len(input)==0: return 1
  	i = 0
  	while i <len(input):
  		if input[i]<1 or input[i]>len(input):
  			i+=1
  			continue
  		if input[i]!=input[input[i]-1]:#exchange num, let the element at this index to be the supposed value, ex. index 2->number 3
  			temp = input[input[i]-1]
  			input[input[i]-1] = input[i]
  			input[i]=temp
  			continue
  		i+=1
  	res,i = 1,0
  	while i<len(input) and res == input[i]:
  		res+=1
  		i+=1
  	return res


#https://leetcode.com/problems/first-missing-positive/description/