class Solution(object):
  def addBinary(self, a, b):
  	a,b=list(a),list(b)
  	length = max(len(a), len(b))
  	if len(a)<length:
  		more = length-len(a)
  		for i in range(more):
  			a.insert(0,"0")
  	if len(b)<length:
  		more = length-len(b)
  		for i in range(more):
  			b.insert(0,"0")
  	res,plus= [],0
  	for i in range(1,len(a)+1):
  		temp1,temp2 = int(a[-i]),int(b[-i])
  		bit = temp1+temp2+plus
  		if bit>=2:
  			plus = 1
  			bit-=2
  		else:plus = 0
  		res.insert(0,str(bit))
  	if plus == 1: res.insert(0,"1")
  	return "".join(res)


if __name__ == "__main__":
    s = Solution()
    s.addBinary("11010","1010")