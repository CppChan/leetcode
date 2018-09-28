class Solution(object):
  def removeInvalidParentheses(self, s):
  	left,right=0,0
  	for i in range(len(s)):
  		if s[i]=='(':left+=1
  		elif s[i]==')':right+=1
  	res,now = 0,0
  	for i in range(len(s)):
  		if s[i]=='(':now+=1
  		if s[i]==')':
  			if now>0:
  				now-=1
  				res+=1
  	fin=set([])
  	self.dfs(s, 0,0, res, left-res, right-res, fin, "",0)
  	return list(fin)
  def dfs(self, s, i, now, res, resume1, resume2, fin, temp,notnum):
  	if (len(temp)-notnum)/2>=res:
  		if now == 0:
  			fin.add(temp)
  		return
  	if i == len(s) and (now!=0 or len(temp-notnum)/2!=res):return
  	if s[i]=='(':
  		if resume1>0:self.dfs(s, i+1, now, res, resume1-1, resume2, fin, temp,notnum)
  		self.dfs(s, i+1, now+1, res, resume1, resume2, fin, temp+'(',notnum)
  	elif s[i]==')':
  		if now==0:
  			if resume2==0:return
  			self.dfs(s,i+1,now,res,resume1,resume2-1,fin,temp,notnum)
  		else:
  			if resume2>0:
  				self.dfs(s, i+1, now, res, resume1, resume2-1, fin, temp,notnum)
  			self.dfs(s, i+1, now-1,res,resume1, resume2, fin, temp+')',notnum)
  	else:
  		self.dfs(s, i+1, now, res, resume1, resume2, fin, temp+s[i],notnum+1)
  	return