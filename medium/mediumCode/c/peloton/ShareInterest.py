from collections import defaultdict
class Solution(object):
  def shareinterest(self, From, to, weight):
  	connect_count, max_connect, maxproduct = defaultdict(lambda:0),0,0
  	for i in range(len(From)):
  		pair = (min(From[i],to[i]),max(From[i],to[i]))
  		connect_count[pair]+=1
  		if connect_count[pair]>=max_connect: maxproduct = max(maxproduct, pair[0]*pair[1])
  		if connect_count[pair]>max_connect: max_connect = connect_count[pair]
  	return maxproduct

if __name__ == "__main__":
    s = Solution()
    print s.shareinterest([2,1,1,2,2],[3,2,2,3,4],[1,2,1,3,3])