class Solution(object):
  def songtime(self, input):
  	count,res,dic= [0,0],0,{}
  	for i in range(len(input)):
  		if input[i]==0:count[0]+=1
  		elif input[i]%60==0:count[1]+=1
  		else:
  			input[i]=input[i]%60
  			if input[i] not in dic: dic[input[i]]=1
  			else: dic[input[i]]+=1
  	res+=(count[0]*count[1]+(count[1]*(count[1]-1)/2))
  	for i in range(len(input)):
  		if input[i]==0 or input[i]%60==0 or input[i] not in dic:continue
  		if input[i]==30:
  			res+=dic[input[i]]*(dic[input[i]]-1)/2
  			dic.__delitem__(input[i])
  		else:
  			if  60-input[i] in dic:
  				res+=dic[input[i]]*dic[60-input[i]]
  				dic.__delitem__(input[i])
  				dic.__delitem__(60-input[i])
  	return res
if __name__ == "__main__":
    s = Solution()
    print s.songtime([60,120,60,0,0,34,26,121,59,21,21,30])
    print s.songtime([60,60,60])