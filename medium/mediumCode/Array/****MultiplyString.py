class Solution(object):
  def multiply(self, num1, num2):
  	length = len(num1)+len(num2)
  	dic = {}
  	for i in range(length):
  		dic[i]=[]
  	if len(num1)<len(num2):num1,num2=num2,num1
  	for j in range(len(num2)):
  		for i in range(len(num1)):
  			temp = str(int(num1[i])*int(num2[j]))
  			gap = len(num1)-i-1+len(num2)-j-1
  			dic[length-gap-1].append(int(temp[-1]))
  			if len(temp)>1: dic[length-gap-2].append(int(temp[0]))
  	res,plus= [],0
  	for i in range(length-1,-1,-1):
  		bit = 0
  		for j in range(len(dic[i])):
  			bit+=dic[i][j]
  		bit+=plus
  		if i == 0 and bit == 0:break
  		bit = str(bit)
  		res.insert(0,bit[-1])
  		if bit[0:len(bit)-1]: plus = int(bit[0:len(bit)-1])
  		else:plus = 0
  	while len(res)>1 and res[0]=='0':#corner case: like 123*0
  		res.pop(0)
  	return "".join(res)


#https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation