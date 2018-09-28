class Solution(object): # find A+B = D-C
  def exist(self, array):
  	array = sorted(array)
  	if len(array)<4:return False
  	dif = [0]*(len(array)-1)
  	for i in range(1,len(array)):
  		dif[i-1]=array[i]-array[i-1]
  	for i in range(len(array)-1):
  		for j in range(i+1, len(array)):
  			target = array[i]+array[j]
  			newdif = dif[:]
  			if i == 0:newdif.pop(0)
  			else:
  				newdif[i] = newdif[i-1]+newdif[i]
  				newdif.pop(i-1)
  			if j == 1: newdif.pop(0)
  			elif j == len(array)-1: newdif.pop(len(newdif)-1)
  			else:
  				newdif[j-1] = newdif[j-2]+newdif[j-1]
  				newdif.pop(j-2)
  			if self.find(newdif, target):return True
  	return False

  def find(self, array, target):
  	i,j=0,0
  	temp = array[0]
  	while i<=j and i<len(array) and j<len(array):
  		if temp==target: return True
  		elif temp<target:
  			if j == len(array)-1: return False
  			j+=1
  			temp+=array[j]
  		else:
  			if i == j and i<len(array)-1:
  				temp = array[i+1]
  				i+=1
  				j+=1
  				continue
  			elif i == j and i==len(array)-1:return False
  			temp-=array[i]
  			i+=1
  	return False