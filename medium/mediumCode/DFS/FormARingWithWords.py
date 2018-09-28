class Solution(object):
  def formRing(self, input):
  	if len(input)==0:return False
  	if len(input)==1:
  		if input[0][0]==input[0][-1]:return True
  		else:return False
  	return self.dfs(input[1:len(input)], input[0])

  def dfs(self, input, temp):
  	if len(input)==1:
  		if input[0][0]==temp[-1] and input[0][-1]==temp[0]:return True
  		return False
  	for i in range(len(input)):
  		if temp[-1]==input[i][0]:
  			now = input[i]
  			input.pop(i)
  			if self.dfs(input, temp+now):return True
  			input.insert(i, now)
  	return False