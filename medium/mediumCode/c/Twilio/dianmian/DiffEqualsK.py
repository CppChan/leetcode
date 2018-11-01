class Solution(object):
  def diffequalsk1(self,input, k):
  	dic,res= {},[]
  	for i in range(len(input)):
  		if input[i] in dic:
  			for j in dic[input[i]]:
  				res.append((j, i))
  		if input[i]+k in dic: dic[input[i]+k].append(i)
  		else: dic[input[i]+k] = [i]
  		if input[i]-k in dic: dic[input[i]-k].append(i)
  		else: dic[input[i]-k] = [i]
  	return res

  def diffequalsk2(self, input, k):
      for i in range(len(input)):
        input[i]=(i, input[i])
      input = sorted(input, key = lambda x:x[1])
      res,i,j = [],0,1
      while i<j and j<len(input):
        while j<len(input):
            if input[j][1]-input[i][1]>=k:break
            j+=1
        while i<j:
            if input[j][1]-input[i][1]<=k:break
            i+=1
        if input[j][1]-input[i][1]==k:
            pre, back,start,end = input[i][1],input[j][1],j,None
            while i<j and input[i][1]==pre:
                while j<len(input) and input[j][1]==back:
                    res.append((input[i][0],input[j][0]))
                    j+=1
                end = j
                j = start
                i+=1
            j = end
      return res





if __name__=="__main__":
    s = Solution()
    print s.diffequalsk1([2,5,2,5,4,7,6,-1], 3)
    print s.diffequalsk2([2,5,2,5,4,7,6,-1], 3)
