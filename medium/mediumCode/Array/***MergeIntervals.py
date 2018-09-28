class Solution():
  def length(self, interval):
  	interval, i,time, pre, back= sorted(interval, cmp = self.comp),0,0,interval[0][0],interval[0][1]
  	while i<len(interval):
  		pre, back= max(pre, interval[i][0]), interval[i][1]#corner
  		while i<len(interval)-1 and interval[i][0]==interval[i+1][0]:
  			i+=1
  			back = max(interval[i][1], pre)#corner
  		if back > pre: time+=(back-pre)
  		pre = max(pre,back)#corner
  		i+=1
  	return time

  def comp(self, x, y):
  	if x[0]!=y[0]:return x[0]-y[0]
  	else: return x[1]-y[1]

if __name__ == "__main__":
    s = Solution()
    print s.length([[1,5],[1,9],[2,5],[7,8],[5,6],[8,12],[13,15],[3,8],[5,7],[14,16]])