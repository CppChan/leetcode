class Solution(object):
  def getPermutation(self, n, k):
  	if n == 0: return ""
  	sum = 1
  	series = ""
  	for i in range(1, n+1):
  		sum=sum*i
  		series+=str(i)
  	if k>sum: return ""
	return self.findtarget(sum, k,series)

  def findtarget(self, sum, k,series):
  	if len(series)==1:
  		return series[0]
  	group = sum/len(series)
  	temp = series[(k-1)/group]
  	left = sum/len(series)
  	series = series[0:(k-1)/group]+series[(k-1)/group+1:len(series)]
  	k = k-group*((k-1)/group)
  	return temp+self.findtarget(left, k, series)