class Solution(object):
  def maxDiff(self, array):
  	res = 0
  	for i in range(1,len(array)):
  		temp1,temp2 = array[0:i], array[i:len(array)]
  		dif1, dif2 = abs(self.find(temp1)-(-self.find(self.neg(temp2)))), abs(self.find(temp2)-(-self.find(self.neg(temp1))))#abs!!!
  		if dif1>res: res = dif1
  		if dif2>res: res = dif2
  	return res

  def neg(self, array):
  	newarray = array[:]#dont forget
  	for i in range(len(array)):
  		newarray[i]=-array[i]
  	return newarray

  def find(self,array):
  	dp = [0]*len(array)
  	res = -float('inf')
  	for i in range(len(array)):
  		if i == 0: dp[0]=array[0]
  		else:
  			if dp[i-1]>0: dp[i]= dp[i-1]+array[i]
  			elif dp[i-1]<=0: dp[i]=array[i]
  		if dp[i]>res: res = dp[i]
  	return res