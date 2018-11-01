class Solution(object):
  def find(self, time, input):
  	time = self.merge(time)
	for i in xrange(len(time)):
		if time[i][0]<=input[0] and time[i][1]>=input[1]:return True
	return False

  def merge(self, time):
  	time.sort(key = lambda x: x[0])
  	res = []
  	for i in xrange(len(time)):
  		if len(res)==0 or time[i][0]>res[-1][1]: res.append(time[i])
  		else: res[-1][1] = max(res[-1][1], time[i][1])
  	return res


if __name__=="__main__":
    s = Solution()
    print s.find([[1,7],[8,10],[2,5],[13,18]],[2,6])