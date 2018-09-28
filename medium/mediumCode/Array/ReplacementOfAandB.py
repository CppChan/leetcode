class Solution(object):
  def minReplacements(self, input):
  	if len(input)==0 or len(input)==1: return 0
  	atime, btime= 0, 0
  	for i in range(len(input)):
  		if input[i]=='a':atime+=1
  		else: btime+=1
  	anow, bnow, res = 0, 0, atime
  	for i in range(len(input)):
  		if input[i]=='a': anow+=1
  		else: bnow+=1
  		temp = atime-anow+bnow
  		if temp<res: res = temp
  	return res