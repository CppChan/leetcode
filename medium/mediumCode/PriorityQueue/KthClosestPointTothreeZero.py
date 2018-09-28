import heapq
class Solution(object):
  def closest(self, a, b, c, k):
    i, j, q = 0,0,0
    dd = set([])
    dd.add((0,0,0))
    res = [(a[i]**2+b[j]**2+c[q]**2,i,j,q)]
    heapq.heapify(res)# heap use the first element in tuple to sort( by default)
    for d in range(k-1):
      temp = heapq.heappop(res)
      if temp[1]+1<len(a) and (temp[1]+1, temp[2], temp[3]) not in dd :
        heapq.heappush(res, (a[temp[1]+1]**2+b[temp[2]]**2+c[temp[3]]**2,temp[1]+1, temp[2], temp[3]))
        dd.add((temp[1]+1, temp[2], temp[3]))
      if temp[2]+1<len(b) and (temp[1], temp[2]+1, temp[3]) not in dd:
        heapq.heappush(res, (a[temp[1]]**2+b[temp[2]+1]**2+c[temp[3]]**2, temp[1], temp[2]+1, temp[3]))
        dd.add((temp[1], temp[2] + 1, temp[3]))
      if temp[3]+1<len(c) and (temp[1], temp[2], temp[3]+1) not in dd:
        heapq.heappush(res, (a[temp[1]]**2+b[temp[2]]**2+c[temp[3]+1]**2, temp[1], temp[2], temp[3]+1))
        dd.add((temp[1], temp[2], temp[3]+1))
    new = heapq.heappop(res)
    return [a[new[1]], b[new[2]], c[new[3]]]



if __name__ == "__main__":
    s = Solution()
    print s.closest([1,2,3],[2,4],[1,2],10)