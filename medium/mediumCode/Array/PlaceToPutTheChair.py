class Solution(object):
  def putChair(self, gym):
  	row, col = [0]*len(gym),[0]*len(gym[0])
  	for i in range(len(gym)):
  		for j in range(len(gym[i])):
  			if gym[i][j]=="E":
  				row[i]+=1
  				col[j]+=1
  	return [self.compute(row), self.compute(col)]

  def compute(self, list):
  	if len(list)==1:return 0
  	sumlist,temp,sum= [0]*len(list),0,0
  	for i in range(len(list)):
  		sum+=i*list[i]
  		temp+=list[i]
  		sumlist[i] = temp
  	temp, res, index= sum, sum,0
  	for i in range(1,len(list)):
  		temp = temp+sumlist[i-1]*2-sumlist[-1]
  		if temp<res:
  			res = temp
  			index = i
  	return index

# make a row array and col array represent how many chairs in this certain row/col
# compute prefix sum and use temp = temp+sumlist[i-1]*2-sumlist[-1] to compute cost