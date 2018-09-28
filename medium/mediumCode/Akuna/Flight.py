import heapq
class tuple(object):
	def __init__(self, city, count):
		self.city = city
		self.count = count
	def __cmp__(self, other):
		if self.count == other.count:return cmp(self.city, other.city)
		return other.count - self.count
class Solution(object):
  def process(self, input):
  	res, pq, dic, maxdist, maxnum, accudist= [], [],{},0,"",0
  	heapq.heapify(pq)
  	for i in range(len(input)):
  		temp = input[i].split(":")
  		flightnum, begin, end, dist = temp[0],temp[1],temp[2],temp[3]
  		accudist +=int(dist)
  		if int(dist)>maxdist:
  			maxdist,maxnum = int(dist), flightnum
		if begin not in dic:
			dic[begin]=tuple(begin,1)
			heapq.heappush(pq, dic[begin])
		else: dic[begin].count+=1
		if end not in dic:
			dic[end]=tuple(end,1)
			heapq.heappush(pq, dic[end])
		else: dic[end].count+=1
		heapq.heapify(pq)#here is important, must heapify, heappush will heapify, this will notX
  		res.append(str(accudist)+":"+maxnum+":"+pq[0].city)
  	return res


if __name__=="__main__":
    s = Solution()
    print s.process(["C0FFEE1C:CHI:NYC:714","OFFICE18:LA:SEATLE:961","COFFEE1C:NYC:LA:2448","DDDDD:NYC:GUANGZHOU:211","DDDDD:LA:GUANGZHOU:21111"])