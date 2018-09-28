class Solution(object):
  def productExceptSelf(self, nums):
  	if len(nums)==1:return nums
  	res = [1]*len(nums)
  	product = 1
  	for i in range(1, len(nums)):
  		product = product*nums[i-1]
  		res[i]=product
  	product = 1
  	for i in range(len(nums)-2, -1,-1):
  		product = product*nums[i+1]
  		res[i]=res[i]*product
  	return res