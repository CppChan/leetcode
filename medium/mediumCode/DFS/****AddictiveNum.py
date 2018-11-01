class Solution(object):
  def isAdditiveNumber(self, list):
  	if len(list)<3:return False
  	return self.find(list, 0, 0,0)
  def find(self, list, pre, num, preone): # pre is previous two , preone is previous one
  	if len(list)==0:return True
  	if num == 0: #num means the number of round, here is the first level of dfs
  		if list[0]=='0':return self.find(list[1:len(list)], 0,1,0)#corner
  		for i in range(1,(len(list)/2)+1):#corner if len(list)==3 then must +1
  			if self.find(list[i:len(list)], int(list[0:i]),1,int(list[0:i])):return True
  		return False
  	elif num == 1:
  		if list[0]=='0':return self.find(list[1:len(list)], pre,1,0)#corner
  		for i in range(1,len(list)-len(str(pre))+1):#corner if len(list)==3 then must +1
  			if self.find(list[i:len(list)], pre+int(list[0:i]),num+1, int(list[0:i])):return True
  		return False
  	else:
  		if list[0]=='0' and int(list[0])==pre:return self.find(list[1:len(list)], 0+preone, num+1, 0)#corner
  		if len(str(pre))<=len(list) and list[0:len(str(pre))]==str(pre) and self.find(list[len(str(pre)):len(list)], pre+preone, num+1, pre):return True
  		return False
if __name__ == "__main__":
    s = Solution()
    print s.isAdditiveNumber("199100199")