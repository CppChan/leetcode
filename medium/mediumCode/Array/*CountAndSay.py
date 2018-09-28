class Solution(object):
  def countAndSay(self, n):
  	i, pre, new= 1, "1", ""
  	while i<n:
  		pre = self.count(pre)
  		i+=1
  	return pre

  def count(self, pre):
  	res, count, i="", 0, 0
  	while i<len(pre):
		if i!=0 and pre[i]!=pre[i-1]:
  			res+=(str(count)+pre[i-1])
  			count = 1#pay attention here not count = 0, should count current element
  		else:
  			count+=1
  		i+=1
  	if count>0:res=res+(str(count)+pre[-1])
  	return res