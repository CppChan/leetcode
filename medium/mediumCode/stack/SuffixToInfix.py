class Solution(object):
  def convert(self, suffix):
  	stack = []
  	list = suffix.split(' ')
  	i = 0
  	pre = ''
  	while i<len(list):
  		while list[i].isdigit():
  			stack.append(list[i])
  			i+=1
  		temp1 = stack.pop()
  		temp2 = stack.pop()
  		if (pre == '+' or pre == '-') and (list[i]=='*'or list[i]=='/'):
  			newtemp = temp2+list[i]+'('+temp1+')'
  			pre = list[i]
  			stack.append(newtemp)
  		else:
  			newtemp = temp2+list[i]+temp1
  			pre = list[i]
  			stack.append(newtemp)
  		i+=1
  	return stack.pop()