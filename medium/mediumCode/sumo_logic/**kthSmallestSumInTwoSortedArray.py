import heapq
class tuple(object):
	def __init__(self, i, j, val):
		self.i = i
		self.j = j
		self.val = val
	def __cmp__(self,other):
		return cmp(self.val, other.val) # if define this, when call 'if sth in heap', it will use val to check if there is repeatance
class Solution(object):
  def kthSum(self, A, B, k):
  	num = 0
  	isgo = [[0]*len(B) for i in range(len(A))]#used to avoid visiting same pair twice.!!!!!!!!!
  	heap = [tuple(0,0,A[0]+B[0])]
  	heapq.heapify(heap)
  	while num<k-1:
  		temp = heapq.heappop(heap)
  		if temp.i+1<=len(A)-1 and isgo[temp.i+1][temp.j]==0:
  			heapq.heappush(heap, tuple(temp.i+1, temp.j, A[temp.i+1]+B[temp.j]))
  			isgo[temp.i+1][temp.j]=1
  		if temp.j+1<=len(B)-1 and isgo[temp.i][temp.j+1]==0:
				heapq.heappush(heap, tuple(temp.i, temp.j+1, B[temp.j+1]+A[temp.i]))
				isgo[temp.i][temp.j+1]=1
  		num+=1
  	return heapq.heappop(heap).val

if __name__ == "__main__":
    S = Solution()
    print S.kthSum([1,3,5,8,9],[2,3,4,7],6)
