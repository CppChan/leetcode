class Solution(object):
  def solvemine(self, input):
  	res, mine= [[0]*len(input[0]) for i in range(len(input))],[]
  	for i in range(len(input)):
  		for j in range(len(input[0])):
  			if input[i][j]=="m":mine.append((i,j))
  	self.roundone(res,mine)
  	self.roundtwo(res,mine)
  	self.roundthree(res,mine)
  	self.roundfour(res,mine)
  	self.roundfive(res,mine)
  	self.roundsix(res,mine)
  	return res

  def roundone(self,res,mine):
  	for m in mine:
  		i,j=m[0],m[1]
  		if i-1>=0: res[i-1][j]+=1
  		if i+1<len(res):res[i+1][j]+=1
  		if j-1>=0: res[i][j-1]+=1
  		if j+1<len(res[0]):res[i][j+1]+=1
  		if i-1>=0 and j-1>=0: res[i-1][j-1]+=1
  		if i-1>=0 and j+1<len(res[0]): res[i-1][j+1]+=1
  		if i+1<len(res) and j-1>=0: res[i+1][j-1]+=1
  		if i+1<len(res) and j+1<len(res[0]): res[i+1][j+1]+=1

  def roundtwo(self,res, mine):
  	for m in mine:
  		i,j=m[0],m[1]
  		if i+1<len(res):res[i+1][j]=2

  def roundthree(self,res,mine):
  	for m in mine:
  		i,j=m[0],m[1]
  		if j+1<len(res[0]):res[i][j+1]=0

  def roundfour(self,res, mine):
  	isTriple = [False]*len(res)
  	for m in mine:
  		i,j=m[0],m[1]
  		if i%2!=0:
  			if isTriple[i]==True:continue
  			isTriple[i]=True
  			for k in range(len(res[0])):
  				res[i][k]=res[i][k]*3

  def roundfive(self,res, mine):
  	count = [[0]*len(res[0]) for i in range(len(res))]
  	for m in mine:
  		i,j=m[0],m[1]
  		if i-1>=0 and j-1>=0: count[i-1][j-1]+=1
  		if i-1>=0 and j+1<len(res[0]): count[i-1][j+1]+=1
  		if i+1<len(res) and j-1>=0: count[i+1][j-1]+=1
  		if i+1<len(res) and j+1<len(res[0]): count[i+1][j+1]+=1
  	for i in range(len(count)):
  		for j in range(len(count[0])):
  			if count[i][j]>=1:res[i][j]=res[i][j]*2

  def roundsix(self,res, mine):
  	for m in mine:
  		i,j=m[0],m[1]
  		res[i][j]=-1

if __name__ == "__main__":
    s = Solution()
    print s.solvemine([[1,'m',1,1],[1,1,1,1],[1,1,1,'m'],['m',1,1,1]])