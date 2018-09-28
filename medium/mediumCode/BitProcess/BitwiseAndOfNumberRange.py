class Solution(object):
  def rangeBitwiseAnd(self, m, n):
  	temp = m
  	for i in range(m+1, n):
  		temp = temp&i# '|' is huo
  	return temp