class Solution(object):
  def rob(self, nums):
  	if len(nums)<1:return 0
  	if len(nums)==1:return nums[0]
  	nums1, nums2 = nums[1:len(nums)], nums[0: len(nums)-1]
  	return max(self.compute(nums1), self.compute(nums2))

  def compute(self, nums):
  	dp = [0]*(len(nums)+1)
  	dp[0],dp[1]=0,nums[0]
  	for i in range(2, len(nums)+1):
  		dp[i]=max(nums[i-1]+dp[i-2], dp[i-1])
  	return dp[len(nums)]