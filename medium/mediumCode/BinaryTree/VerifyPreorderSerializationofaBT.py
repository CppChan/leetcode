class Solution(object):
  def isValidSerialization(self, preorder):
  	list = preorder.split(',')
  	if len(list)==0:return False
  	if len(list)==1 and list[0]=='#': return True
  	stack = [list[0]]
  	for i in range(1,len(list)):
  		if len(stack)==0:return False
  		if not self.addup(stack, list[i]): return False
  	if len(stack)!=0: return False
  	else: return True

  def addup(self, stack, item):
  	if len(stack)==0:return True
  	if stack[-1]!='#' or item!='#':
  		stack.append(item)
  		return True
  	else:
  		stack.pop()
  		if len(stack)==0:return False
  		else:
  			stack.pop()
  			return self.addup(stack, '#')