class Solution(object):
  def minJump(self, array, index):
  	if index == len(array)-1:
  		return 0
  	indextotal = set([index])
  	indextemp = [index]
  	return self.findmin(array, indextotal, indextemp)

  def findmin(self, array, indextotal, indextemp):
  	newindextemp = []
  	for i in indextemp:
  		for j in range(1,array[i]+1):
  			if (i-j>=0 and i-j not in indextotal and array[i-j]!=0):
  				indextotal.add(i-j)
  				newindextemp.append(i-j)
  			if(i+j==len(array)-1):
  				return 1
  			elif(i+j<len(array)-1 and i+j not in indextotal and array[i+j]!=0):
  				indextotal.add(i+j)
  				newindextemp.append(i+j)
  	if len(newindextemp)==0:
  		return -1
  	else:
  		temp = self.findmin(array, indextotal, newindextemp)
  		if(temp==-1):
  			return -1
  		else:
  			return 1+temp