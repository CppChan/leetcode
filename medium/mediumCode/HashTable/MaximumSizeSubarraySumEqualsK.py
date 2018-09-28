class Solution(object):
  def maxSubArrayLen(self, nums, k):
  	if k ==0:return 0#corner
  	sumlist, temp, maxlength= [],0,-1
  	for i in range(len(nums)):
  		temp+=nums[i]
  		sumlist.append(temp)
  		if temp == k: maxlength=i+1
  	dic = {}
  	for i in range(len(sumlist)):
  		if dic.has_key(sumlist[i]) and i-dic[sumlist[i]]>maxlength: maxlength = i-dic[sumlist[i]]
  		if dic.has_key(sumlist[i]+k):continue
  		else: dic[sumlist[i]+k]=i
  	return maxlength