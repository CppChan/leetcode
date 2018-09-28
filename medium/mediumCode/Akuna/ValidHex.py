class Solution(object):
  def isvalid(self, input):
  	if len(input)<=2:return False
  	return self.compute(input[:len(input)-2])==int("0x"+input[len(input)-2:],16)

  def compute(self, input):
  	temp = str(int("0x"+str(input), 16))
  	res = 0
  	for i in range(len(temp)):
  		res+=int(temp[i])
  	return res


if __name__=="__main__":
    s = Solution()
    print s.isvalid("C0FFEE1C")
    print str(hex(16))[2:]
    print int("0xC0ffEE",16)