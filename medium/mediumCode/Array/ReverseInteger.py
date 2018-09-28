class Solution(object):
  def reverse(self, x):
  	if abs(x)<10:return x
  	if abs(x)>=1000000003:return 0
  	neg = False
  	if x<0:neg = True
  	x = str(abs(x))
  	while len(x)>0 and x[-1]=="0":
  		x = x[0:len(x)-1]
  	res = ""
  	for i in range(len(x)-1,-1,-1):
  		res+=(x[i])
  	res = int(res)
  	if neg:return -res
  	return res