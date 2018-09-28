class Solution(object):
  def numOfWords(self, input):
  	res,over= 0, True
  	for i in range(len(input)):
  		if over and input[i] not in (" ","\n","\t"):
  			res+=1
  			over = False
  		elif not over and input[i] in (" ","\n","\t"): over = True
  	return res