class Solution(object):
  def removeComments(self, source):
  	res, buffer, inblock= [],[], False
  	for i in range(len(source)):
  		j, line, temp, tempbuffer = 0, source[i],[],[]
  		while j<len(line):
  			if line[j:j+2]=="/*" and not inblock and len(buffer)==0:
  				tempbuffer.append("/*")#corner case
  				inblock= True
  				j+=2#must plus 2
  			elif line[j:j+2]=="*/" and inblock:
  				if len(buffer)==0:temp.append(" ")
  				else: res.append([" "]*(len(buffer)+1))
  				inblock, tempbuffer, buffer= False,[], []
  				j+=2
  			elif line[j:j+2]=="//":
  				k = j
  				while k<len(line):#corner, for case like "/* xxxx", "//xxxxxxx */", dont eliminate the second sentence
  					if inblock and line[k:k+2]=="*/":
  						j = k
  						break
  					k+=1
  				if k == len(line):
  					temp.append(" ")
  					break
  			elif inblock:
  				tempbuffer.append(line[j])
  				j+=1
  			else:
  				temp.append(line[j])
  				j+=1
  		if len(temp)>0: res.append("".join(temp))
  		if len(tempbuffer)>0: buffer.append("".join(tempbuffer))
  	if len(buffer)>0: res.extend(buffer)
  	return res


  def removeComments2(self, source):# ordinary, for all /* must have a */
	  in_block = False
	  ans = []
	  for line in source:
		  i = 0
		  if not in_block:
			  newline = []
		  while i < len(line):
			  if line[i:i + 2] == '/*' and not in_block:
				  in_block = True
				  i += 1
			  elif line[i:i + 2] == '*/' and in_block:
				  in_block = False
				  i += 1
			  elif not in_block and line[i:i + 2] == '//':
				  break
			  elif not in_block:
				  newline.append(line[i])
			  i += 1
		  if newline and not in_block:
			  ans.append("".join(newline))

	  return ans

if __name__=="__main__":
    s=Solution()
    print s.removeComments(["public class hellowworld(){", "//This program", "public static void main(String args[]){ ", "System.out.print(hello/*world*/); //A single line comment", "/* a sample comment", "sample comment", "comment*/", "/*}", "}"])