from collections import deque
class Soluton(object):
  def planting(self, pathLength, floristInterval):
  	floristInterval.sort(key = lambda x: x[1])
  	queue,res = deque([]),0
  	for i in range(len(floristInterval)):
  		if floristInterval[i][1]< 0 or floristInterval[i][0]>=pathLength: continue
  		if len(queue)<3:
  			queue.append(floristInterval[i])
  			res+=1
  		else:
  			if floristInterval[i][0]<queue[0][1]:continue
  			else:
  				queue.popleft()
  				queue.append(floristInterval[i])
  				res+=1
  	return res

if __name__ == "__main__":
    s = Soluton()
    print s.planting(9,[[1,10],[1,6],[2,8],[3,5],[5,6],[7,11],[0,4],[4,9]])