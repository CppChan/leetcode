class Solution(object):
  def minSubArrayLen(self, s, nums):
  	if len(nums)==0 and s>0: return 0
  	if len(nums)==1 and s>nums[0]: return 0
  	temp = nums[0]
  	i, j, res= 0,0,float('inf')
  	while i<=j and j < len(nums):
  		if i == j and temp>=s: return 1
  		if temp<s:
  			if j < len(nums)-1:
  				j+=1
  				temp+=nums[j]
  			else: break
  		elif temp>=s:
  			if j-i+1<res: res = j-i+1
  			i+=1
  			temp-=nums[i-1]
  	if res<float('inf'):return res
  	else: return 0