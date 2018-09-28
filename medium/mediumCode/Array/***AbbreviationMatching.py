class Solution(object):
  def match(self, input, pattern):
  	start = 0
  	i = 0
  	for i in range(len(pattern)):
  		if start>=len(input): break#corner case
  		elif pattern[i].isalpha():
  			if pattern[i]!=input[start]:return False
  			else:
  				start+=1
  		else:
  			j = i
  			while j<len(pattern) and pattern[j].isdigit():#!!!!!!
  				j+=1
  			start+=int(pattern[i:j])
  	if start!=len(input) or i<len(pattern)-1:return False#corner case
  	else:return True