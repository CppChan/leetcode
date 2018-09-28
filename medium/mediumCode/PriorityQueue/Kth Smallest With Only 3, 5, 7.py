import heapq
class Solution(object):
  def kth(self, k):
    res = []
    res.append(3*5*7)
    heapq.heapify(res)
    for i in range(k-1):
      temp = heapq.heappop(res)
      if temp*3 not in res:
        heapq.heappush(temp*3)
      if temp*5 not in res:
        heapq.heappush(temp*5)
      if temp*7 not in res:
        heapq.heappush(temp*7)
    return heapq.heappop(res)