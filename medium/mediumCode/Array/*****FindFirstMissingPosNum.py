class Solution(object):
  def firstMissingPositive(self, server):
  	n = len(server)
  	for i in range(n):
  		while server[i]>0 and server[i]<=n and server[server[i]-1]!=server[i]:
  			swap = server[i]-1
  			server[i],server[swap] = server[swap],server[i]
  	for i in range(len(server)):
  		if server[i]!=i+1:return i+1
  	return n+1

if __name__ == "__main__":
	s = Solution()
	print s.firstMissingPositive2([3,4,-1,1])


# https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c++-solution-O(1)-space-and-O(n)-time