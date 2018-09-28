class Solution(object):
  def longestCommonPrefix(self, strs):
  	if len(strs)==0:return ""
  	if len(strs)==1:return strs[0]
  	mid = (0+len(strs))/2
  	left = self.longestCommonPrefix(strs[0:mid])
  	right = self.longestCommonPrefix(strs[mid:len(strs)])
  	return self.findcommon(left,right)

  def findcommon(self, left, right):
  	res = ""
  	for i in range(min(len(left), len(right))):
  		if left[i]==right[i]:res+=left[i]
  		else: break
  	return res