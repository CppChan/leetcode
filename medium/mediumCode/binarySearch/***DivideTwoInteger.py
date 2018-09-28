class Solution(object):
  def divide(self, a, b):
  	if b == 0:return 2147483647
  	if a == 0 or abs(a)<abs(b):return 0
  	neg = False
  	if (a<0 and b>0) or (a>0 and b<0):
  		neg = True
  	a,b=abs(a),abs(b)
  	if a==b:
  		if neg:return -1
  		else:return 1
  	i,j=0, a
  	while i<j-1:
  		mid = (i+j)/2
  		if b*mid==a:
  			if neg:return -1*mid#pay attention cannot writ res = mid, break
  			else:return mid
  		elif b*mid>a: j=mid-1
  		else: i = mid
  	if j*b<=a:res = j#when b == 1
  	else:res = i
  	if neg:return -1*res
  	return res