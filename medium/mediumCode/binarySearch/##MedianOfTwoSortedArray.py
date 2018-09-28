class Solution(object):#Leetcode #4 solution
  def median(self, a, b):
  	if len(a)>len(b):
  		a,b = b,a
  	left, right, all= 0, len(a), (len(a)+len(b))/2
  	while left<=right:
  		i = ((left+right)/2)
  		j = all-i
  		if i>0 and a[i-1]>b[j]:
  			right = i-1
  		elif i<len(a) and b[j-1]>a[i]:
  			left = i+1
  		else:
  			maxleft, minright = 0,0
  			if i == 0:
  				maxleft = b[j-1]
  			elif j ==0:
  				maxleft = a[i-1]
  			else:
  				maxleft = max(a[i-1], b[j-1])
  			if (len(a)+len(b))%2==1:
  				return maxleft
  			if i==len(a):
  				minright = b[j]
  			elif j == len(b):
  				minright = a[i]
  			else:
  				minright = min(b[j], a[i])
  			return (maxleft+minright)/2.0