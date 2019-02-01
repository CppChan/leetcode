class Solution():
  def length(self, interval):
	#pre is the ending time of previous stage
  	interval, i,time, pre, back= sorted(interval, cmp = self.comp),0,0,interval[0][0],interval[0][1]
  	while i<len(interval):
  		pre, back= max(pre, interval[i][0]), interval[i][1]# if interval[i][0]> pre, then we skip the gap between interval[i][0] and pre
  		while i<len(interval)-1 and interval[i][0]==interval[i+1][0]:
  			i+=1
  			back = max(interval[i][1], pre)# if interval[i][1]>pre, then there will be more time
  		if back > pre: time+=(back-pre)
  		pre = max(pre,back)# pre may be updated
  		i+=1
  	return time

  def comp(self, x, y):
  	if x[0]!=y[0]:return x[0]-y[0]
  	else: return x[1]-y[1]

if __name__ == "__main__":
    s = Solution()
    print s.length([[1,5],[1,9],[2,5],[7,8],[5,6],[8,12],[13,15],[3,8],[5,7],[14,16]])