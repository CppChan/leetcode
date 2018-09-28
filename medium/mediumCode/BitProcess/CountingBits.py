class Solution(object):
  def countBits(self, num):
  	if num<1:return [0]
  	temp, twolist,res,i, prelength= 2, [0],[0,1],2,2
  	while i < num+1:
  		prelength,j= i,0
  		while j<prelength and i <num+1:
  			res.append(res[j]+1)
  			i+=1
  			j+=1
  	return res