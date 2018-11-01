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

def s( x, y):
	return x[0]-y[0]

a = [(1,2),(0,1)]
a.sort(key = lambda x: x[0])
print a


# so , when need to specify sorting rules between two variable , use sort(cmp = ...), otherwise, use sort(key = lambda x:x...)