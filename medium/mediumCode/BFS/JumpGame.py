class Solution(object):
  # def minJump1(self, array, index):#method1, initial in a random index, you can jump left or jump right
  # 	if index == len(array)-1:
  #       return 0
  # 	indextotal = set([index])
  # 	indextemp = [index]
  # 	return self.findmin(array, indextotal, indextemp)
  #
  # def findmin(self, array, indextotal, indextemp):
  # 	newindextemp = []
  # 	for i in indextemp:
  # 		for j in range(1,array[i]+1):
  # 			if (i-j>=0 and i-j not in indextotal and array[i-j]!=0):
  # 				indextotal.add(i-j)
  # 				newindextemp.append(i-j)
  # 			if(i+j==len(array)-1):
  # 				return 1
  # 			elif(i+j<len(array)-1 and i+j not in indextotal and array[i+j]!=0):
  # 				indextotal.add(i+j)
  # 				newindextemp.append(i+j)
  # 	if len(newindextemp)==0:
  # 		return -1
  # 	else:
  # 		temp = self.findmin(array, indextotal, newindextemp)
  # 		if(temp==-1):
  # 			return -1
  # 		else:
  # 			return 1+temp

    # method2, initial in first index, only can jump right, use low and high point to indicate
    #the begin and end point of each level in bfs

    def minJump2(self, array):
        low, high, currentmax= 0, 0, 0
        for level in xrange(1,len(array)+1):
            if low>high:
                return -1
            currentmax = 0
            for i in xrange(low, high+1):
                if i+array[i]>=len(array)-1:
                    return level
                else:
                    currentmax = max(currentmax, i+array[i])
            low = high
            high = currentmax
        return -1

if __name__ == "__main__":
    s = Solution()
    print s.minJump2([2,3,1,1,4])
