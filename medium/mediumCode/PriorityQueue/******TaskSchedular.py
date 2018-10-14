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
  	heapq.heapify(list)#sort based on the volume of a task, more volume, first to be handled
  	i,time = 0,0
  	while len(list)>0:
  		temp,i= [],0
  		while i < n+1:#set apart time to be lots of n+1 qujian
  			num = 0
  			if list:
  				num = heapq.heappop(list)#most severe job
  			if num<-1:
  				num+=1#1 task of this kind of job to be handled
  				temp.append(num)# temp is used to store the task to be done in next n+1 qujian
  			time+=1#although len(list)==0, not task to do, which means idle, time still goes by
  			i+=1
  			if len(temp)==0 and len(list)==0:break#corner case, without that will keep add time even though len(list)==0
  		for item in temp:
  			list.append(item)
  	return time


if __name__=="__main__":
	s = Solution()
	s.leastInterval(["A","B","C","A","B"],2)