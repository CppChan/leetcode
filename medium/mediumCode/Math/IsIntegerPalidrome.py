class Solution(object):
  def isPalindrome(self, x):
  	if x<0:return False
  	long,a= 0,1
  	while x/a>0:
  		a=a*10
  		long+=1
  	if long==1 or long==0:return True
  	b, big, small=long/2,10**(long-1), 10
  	for i in range(b):
  		temp1,temp2= (x/big)%10,(x%small)/(10**i)
  		if temp1!=temp2:return False
  		big,small=big/10,small*10
  	return True