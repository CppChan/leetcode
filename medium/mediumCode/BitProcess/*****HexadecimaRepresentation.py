class Solution(object):#could be follow up to every jinzhi
  def hex(self, number):
  	map = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  	return "0x"+self.tohex(number,map)
  def tohex(self, number, map):
  	if number ==0 :return "0"
  	res = ""
  	while number>0:
  		res=map[number&15]+res#number&15 get the number of the last four bit
  		number = number>>4
  	return res