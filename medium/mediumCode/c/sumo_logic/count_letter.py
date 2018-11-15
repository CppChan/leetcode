from collections import defaultdict
class Solution(object):
  def mostcount(self, input):
  	dic, res, max_count= defaultdict(lambda:0), [], 0
  	for i in input:
  		print i
  		dic[i]+=1
  		if dic[i]==max_count: res.append(i)
  		elif dic[i]>max_count: max_count, res = dic[i], [i]
  	return res


s = Solution()
print s.mostcount("")