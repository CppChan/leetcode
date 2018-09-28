class Solution(object):
  def intToRoman(self, num):
  	dic = {1:['I','V','X'],2:['X','L','C'],3:['C','D','M'],4:['M']}
  	num,res=str(num),""
  	for i in range(len(num)):
  		res+=self.compute(int(num[i]),len(num)-i-1,dic)
  	return res

  def compute(self, bit, length,dic):
  	letter = dic[length+1]
  	if bit<=3: return letter[0]*bit
  	elif bit==4:return letter[0]+letter[1]
  	elif bit>=5 and bit<=8:return letter[1]+(bit-5)*letter[0]
  	else:return letter[0]+letter[2]


#https://zhidao.baidu.com/question/326608392028269005.html