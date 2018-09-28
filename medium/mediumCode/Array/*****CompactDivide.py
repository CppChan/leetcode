class Solution(object):
  def divide(self, a, b):
  	isneg = False
  	if (a>0 and b<0) or (a<0 and b>0):
  		isneg = True
  		a,b = abs(a),abs(b)
  	list = {}
  	res = []
  	if b==0:return 'NaN'
  	if a == 0: return '0'
  	res.append(str(a/b))
  	res.append('.')
  	a = (a%b)*10
	begin = self.divided(a, b, list,res,len(res))
  	if not begin:
  		if isneg:res.insert(0,'-')
  		if not list: return "".join(res[0:len(res)-1])
  		else: return "".join(res)
  	else:
  		res.insert(begin, '(')
  		res.append(')')
  		if isneg:res.insert(0,'-')
  		return "".join(res)


  def divided(self,a,b,list,res,index):#corner case!! save beichushu in dict
  	if a == 0: return None
  	temp1, temp2= a/b, a%b
  	if a in list:return list[a]
  	else:
  		list[a]=index
  		res.append(str(temp1))
  	return self.divided(temp2*10,b,list,res,index+1)
