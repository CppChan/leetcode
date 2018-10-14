class Solution(object):
  def strengthenPassword(self, input):
  	for i in range(len(input)):
  		input[i]=self.encode(input[i])
  	return input

  def encode(self, pwd):
  	pwd, length= list(pwd),len(pwd)
  	for i in range(len(pwd)):
  		if pwd[i]=="s" or pwd[i]=="S":pwd[i]='5'
  		if length>1 and length%2!=0 and i>0 and i<length-1 and pwd[i].isdigit(): pwd[i]=str(int(pwd[i])*2)
  	pwd = list("".join(pwd))
  	if len(pwd)>=2 and len(pwd)%2==0:
  		pwd[0],pwd[-1]=pwd[-1],pwd[0]
  		if pwd[0].isalpha() and pwd[0].isupper(): pwd[0] = pwd[0].lower()
  		elif pwd[0].isalpha() and pwd[0].islower(): pwd[0] =pwd[0].upper()
  		if pwd[-1].isalpha() and pwd[-1].isupper(): pwd[-1] = pwd[-1].lower()
  		elif pwd[-1].isalpha() and pwd[-1].islower(): pwd[-1] = pwd[-1].upper()
  	pwd = "".join(pwd)
  	lower_pwd = pwd.lower()
  	pwd = list(pwd)
  	for i in range(len(lower_pwd)):
  		if i+11<=len(lower_pwd) and lower_pwd[i:i+11]=="nextcapital":
  			pwd[i],pwd[i+3],pwd[i+1],pwd[i+2]=pwd[i+3],pwd[i],pwd[i+2],pwd[i+1]
  			break
  	pwd = "".join(pwd)
  	return pwd




if __name__ == "__main__":
    s = Solution()
    print s.strengthenPassword(['GoCardinals', 'Doge', 'nExTcapITalxnextcapital', 'ThreeSThree'])