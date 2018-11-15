class Solution(object):
	def solution(self, stores, house):
		stores.sort()
		for i in range(len(house)):
			house[i]=self.search(house[i], stores)
		return house

	def search(self, h, stores):
		i, j= 0, len(stores)-1
		while i<j-1:
			mid = (i+j)/2
			if h == stores[mid]:return stores[mid]
			if h<stores[mid]: j = mid
			else: i = mid
		if abs(h-stores[i])==abs(h-stores[j]):return min(stores[i], stores[j])
		elif abs(h-stores[i])<abs(h-stores[j]): return stores[i]
		else: return stores[j]

if __name__=="__main__":
    s = Solution()
    print s.solution([1,5,5,5,20,11,11,16,2],[8,18,5,10,17])
    print s.solution([2],[5])
    print s.solution([2,2,2,2,2],[5,12,3,4])
    print s.solution([2,2,3,5,3,6],[0,12,3,4])
    print s.solution([2,2,3,5,3,6],[0,12,3,4])
