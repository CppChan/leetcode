class Solution(object):
  def simplify(self, path):
  	path,stack = path.split("/"),[]
  	for i in range(len(path)):
  		if path[i]=="~": stack = []
  		elif path[i]=="." or path[i]=="": continue # path[i]=="": continue when  '/sd/sdf/fse' then there may be ""
  		elif path[i]=="..":
  			if len(stack)>0:stack.pop()
  		else:stack.append(path[i])
  	return '/'+'/'.join(stack)#remember to put the started '/'