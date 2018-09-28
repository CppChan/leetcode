class Solution(object):
  def calculate(self, s):
  	if len(s)==1:return int(s[0])
  	stack = []
  	pre = None
  	for i in range(len(s)):
  		if s[i]==" ":continue
  		if i == 0:
  			stack.append(s[i])
  			continue
  		if s[i]=="*" or s[i]=="/":
  			pre = s[i]
  			continue
  		if s[i]=="+" or s[i]=="-":
  			stack.append(s[i])
  			pre = None
  			continue
  		else:
  			if not pre: stack.append(s[i])
  			else:
  				temp = stack.pop(-1)
  				if pre=="*":
  					temp = str(int(temp)*int(s[i]))
  					stack.append(temp)
  				elif pre=="/":
  					temp = str(int(temp)/int(s[i]))
  					stack.append(temp)
  	plus = []
  	for i in range(len(stack)):
  		if i==0: plus.append(stack[i])
  		elif stack[i]=="+"or stack[i]=="-":pre=stack[i]
  		else:
  			temp = plus.pop(-1)
  			if pre=="+":
  				temp = str(int(temp)+int(stack[i]))
  				plus.append(temp)
  			elif pre=="-":
  				temp = str(int(temp)-int(stack[i]))
  				plus.append(temp)
  	return int(plus[0])