class Solution(object):
  def isPowerOfTwo(self, number):
  	if number<0:return False#corner case
  	while number>1:
		if number%2==1:return False
  		number = number>>1
  	if number == 1:return True
  	else:return False#when number==0