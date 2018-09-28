class Solution(object):
  def increasingTriplet(self, nums):
  	if len(nums)<3:return False
  	one,two=nums[0],[nums[0],float('inf')]
  	for i in range(1,len(nums)):
  		if nums[i]>two[1]:return True
  		if nums[i]<two[1] and nums[i]>two[0]: two[1]=nums[i]
  		if nums[i]<one:one = nums[i]
  		if nums[i]>one and nums[i]<two[1]:two = [one, nums[i]]
  	return False