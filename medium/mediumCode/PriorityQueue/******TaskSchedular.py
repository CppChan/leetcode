import heapq
class Solution(object):
  def leastInterval(self, tasks, n):
  	if len(tasks)==0:return 0
  	dic = {}
  	for i in range(len(tasks)):
  		if not dic.has_key(tasks[i]):dic[tasks[i]]=1
  		else: dic[tasks[i]]+=1
  	list = []
  	for item in dic.iteritems():
  		list.append(-item[1])
  	heapq.heapify(list)
  	i,time = 0,0
  	while len(list)>0:
  		temp,i= [],0
  		while i < n+1:
  			num = 0
  			if list:
  				num = heapq.heappop(list)
  			if num<-1:
  				num+=1
  				temp.append(num)
  			time+=1
  			i+=1
  			if len(temp)==0 and len(list)==0:break#corner case, without that will keep add time even though len(list)==0
  		for item in temp:
  			list.append(item)
  	return time