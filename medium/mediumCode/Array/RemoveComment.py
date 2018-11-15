class Solution(object):
  def removeComments(self, source):
  	res, buffer, inblock= [],[], False
  	for i in range(len(source)):
  		if not inblock: temp = []
  		j, line, tempbuffer = 0, source[i],[]
  		while j<len(line):
  			if line[j:j+2]=="/*" and not inblock and len(buffer)==0:
  				inblock= True
  				j+=2
  			elif line[j:j+2]=="*/" and inblock:
  				inblock, tempbuffer, buffer= False,[], []
  				j+=2
  			elif line[j:j+2]=="//":
  				k = j
  				while k<len(line):
  					if inblock and line[k:k+2]=="*/":
  						j = k
  						break
  					k+=1
  				if k == len(line): break
  			elif inblock:
  				tempbuffer.append(line[j])
  				j+=1
  			else:
  				temp.append(line[j])
  				j+=1
  		if len(temp)>0 and not inblock: res.append("".join(temp))
  		if len(tempbuffer)>0: buffer.append("".join(tempbuffer))
  	if len(buffer)>0: res.extend(buffer)
  	return res