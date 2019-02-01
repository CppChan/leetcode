import heapq
class position(object):
	def __init__(self, pos, height, left):
		self.pos, self.height, self.left= pos, height, left
	def __cmp__(self, other):
		if self.height == other.height:
			if self.left: return other.pos-self.pos
			else: return self.pos-other.pos
		return self.height-other.height
class Solution(object):
    def pourWater(self, heights, V, K):
    	left,right,lpoint,rpoint,isbreak= [],[], K-1, K+1, False
    	heapq.heapify(left)
    	heapq.heapify(right)
    	while V>0:
    		isbreak = False
    		while lpoint>=0 and heights[lpoint]<=heights[lpoint+1]:
    			heapq.heappush(left, position(lpoint, heights[lpoint], True))
    			lpoint-=1
    		while not isbreak and len(left)>0 and left[0].height<heights[K] and V>0:
    			lmin = heapq.heappop(left)
    			lmin.height+=1
    			heights[lmin.pos]+=1
    			heapq.heappush(left, lmin)
    			V-=1
    			if lpoint>=0 and heights[lpoint]<=heights[lpoint+1]: isbreak = True
    		while not isbreak and rpoint<len(heights) and heights[rpoint]<=heights[rpoint-1]:
    			heapq.heappush(right, position(rpoint, heights[rpoint], False))
    			rpoint+=1
    		while not isbreak and len(right)>0 and right[0].height<heights[K] and V>0:
    			rmin = heapq.heappop(right)
    			rmin.height+=1
    			heights[rmin.pos]+=1
    			heapq.heappush(right, rmin)
    			V-=1
    			if rpoint<len(heights) and heights[rpoint]<=heights[rpoint-1]: isbreak = True
    		if not isbreak and V>0:
    			heights[K]+=1
    			V-=1
    	return heights


if __name__=="__main__":
    s =Solution()
    print s.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],10,2)