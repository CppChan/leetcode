class Solution(object):
  def romanToInt(self, s):
  	dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
  	if len(s)==1:return dic[s]
  	i,j=0,1
  	res = 0
  	while i<len(s) and j<len(s) and i<j:
  		while j<len(s) and dic[s[j]]>=dic[s[j-1]]:
  			j+=1
  		res+=self.compute(dic,s[i:j])
  		i = j
  		j+=1
  	if i==len(s)-1: res+=dic[s[i]]
  	return res
  def compute(self, dic, bit):
  	if len(bit)==1:return dic[bit[0]]
  	i,res= len(bit)-2,dic[bit[-1]]
  	while i>=0 and bit[i]==bit[i+1]:
  		res+=dic[bit[i]]
  		i-=1
  	while i>=0:
  		res-=dic[bit[i]]
  		i-=1
  	return res