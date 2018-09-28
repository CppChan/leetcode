class Solution(object):
  def convert(self, s, nRows):
  	dic = {}
  	for i in range(nRows):
  		dic[i]=[]
  	i,round= 0,1
  	if len(s)==0 or len(s)==1 or nRows==1:return s
  	while i<len(s):
  		while i<len(s) and (i%(2*nRows-2))<nRows and i<round*(2*nRows-2):
  			dic[i%(2*nRows-2)].append(s[i])
  			i+=1
  		index = nRows-2
  		while i<len(s) and (i%(2*nRows-2))<2*nRows-2 and i<round*(2*nRows-2):
  			dic[index].append(s[i])
  			index-=1
  			i+=1
  		round+=1
  	res = []
  	for item in dic.iteritems():
  		res.extend(item[1])
  	return "".join(res)