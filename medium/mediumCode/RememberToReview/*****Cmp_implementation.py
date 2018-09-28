class Solution(object):
  def largestNumber(self, input):
  	input = sorted(input, cmp = self.comp)
  	return ''.join(input)

  def comp(self,x,y):
  	if x==y:return -1
  	i=0
  	for i in range(min(len(x),len(y))):
  		if int(x[i])==int(y[i]):continue
  		return int(y[i])-int(x[i])
  	if i<len(x)-1:
  		return self.comp(x[i+1:len(x)],y)
  	elif i<len(y)-1:
  		return self.comp(x,y[i+1:len(y)])