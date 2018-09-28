class Solution(object):
  def summaryRanges(self, nums):
  	if len(nums)==0: return []
  	if len(nums)==1: return [str(nums[0])]
  	i,j,res=0,1,[]
  	while i<=j and i<len(nums) and j<len(nums):
  		while j<len(nums) and nums[j]-1==nums[j-1]:
  			j+=1
  		if j-1==i:
  			res.append(str(nums[i]))
  		else:
  			res.append(str(nums[i])+"->"+str(nums[j-1]))
  		i = j
  		j+=1
  	if i == len(nums)-1:res.append(str(nums[i]))
  	return res