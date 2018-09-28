class Solution(object):
  def validPostOrder(self, post):
  	if len(post)==0 or len(post)==1:return True
  	return self.ifbinary(post)

  def ifbinary(self, post):
  	if len(post)==1:return True
  	if len(post)==2:
  		if post[0]!=post[1]:return True
  		else:return False
  	root,left,right,divide= post[-1],False,False,0
  	for i in range(1,len(post)-1):
  	  	if post[i]>root:
  			right=True
  			divide = i
  		if post[i-1]==root or post[i]==root or ((post[i-1]>root and post[i]<root)):return False
  	if not right: return self.ifbinary(post[0:len(post)-1])
  	return self.ifbinary(post[0:divide]) and self.ifbinary(post[divide:len(post)-1])