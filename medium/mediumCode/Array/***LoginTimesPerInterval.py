class Solution(object):
  def sessionNum(self, logins):
  	timelist = set([])
  	if len(logins)==0: return []
  	for i in range(len(logins)):
  		timelist.add(logins[i][0])
  		timelist.add(logins[i][1])
  	timelist = list(timelist)
  	timelist = sorted(timelist)
  	dic = {}
  	res = [[0]*3 for i in range(len(timelist)-1)]
  	for i in range(len(timelist)-1):
  		res[i][0]=timelist[i]
  		res[i][1]=timelist[i+1]
  		dic[timelist[i]]=i
  	for i in range(len(logins)):
  		index = dic[logins[i][0]]
  		j = index
  		while j< len(res) and res[j][0]<logins[i][1] and res[j][1]<=logins[i][1]:
  			res[j][2]+=1
  			j+=1
  	i=0
  	while i < len(res):#corner case!! when times equals, combine time interval
  		if res[i][2]==0:
  			res.pop(i)
  			continue
  		elif i<len(res)-1 and res[i][2]==res[i+1][2]:
  			res[i][1]=res[i+1][1]
  			res.pop(i+1)
  			continue
  		i+=1
  	return res