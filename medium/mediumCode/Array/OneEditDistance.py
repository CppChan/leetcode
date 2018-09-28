class Solution(object):
  def oneEditDistance(self, s, t):
  	if s==t:return False
  	if len(s)==len(t):
  		diff = 0
  		for i in range(len(s)):
  			if s[i] != t[i]:diff+=1
  		return diff<=1
  	elif abs(len(s)-len(t))>1:return False
  	if len(s)<len(t):t,s = s,t
  	diff,i,j=False,0,0
  	while i<len(s):
  		if j>=len(t) or s[i]!=t[j]:
  			if diff:return False
  			i+=1
  			diff=True
  			continue
  		i+=1
  		j+=1
  	return True