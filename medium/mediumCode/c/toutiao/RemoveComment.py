class Solution(object):
	def removeComments(self, source):
		res, newline,inblock = [],[],False
		for line in source:
			i = 0
			while i<len(line):
				if line[i:i+2]=="/*" and not inblock:
					inblock = True
					i+=1
				elif line[i:i+2]=="*/" and inblock:
					inblock = False
					i+=1
				elif line[i:i+2]=="//" and not inblock:break
				elif not inblock:
					newline.append(line[i])
				i+=1
			if not inblock :
				if len(newline)>0: res.append("".join(newline))
				newline = []
		return res
