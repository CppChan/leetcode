class Solution(object):
  def wiggleSort(self, nums):
  	median = self.findKthLargest(nums, len(nums)/2)#find median,use quick select
  	n = len(nums)
  	i,left,right =0 ,0,n-1
    #newindex[Left] denotes the position where the next smaller-than median element  will be inserted.
    #newindex[Right] denotes the position where the next larger-than median element  will be inserted.
  	while i<=right:
  		if nums[self.newindex(i,n)]>median:#move the larger than median element to the next newindex(left) place
  			self.swap(nums, self.newindex(i,n), self.newindex(left,n))
  			left+=1
  			i+=1
  		elif nums[self.newindex(i,n)]<median:
  			self.swap(nums, self.newindex(i,n), self.newindex(right,n))#move the small than median element to the next newindex(right) place
  			right-=1
  		else:i+=1
  	return nums

  def swap(self, nums, i, j):
  	nums[i],nums[j]=nums[j], nums[i]

  def newindex(self, i,n):
  	return (1+2*i)%(n|1)

#https://app.laicode.io/app/problem/458

# A = 0011 1100
# B = 0000 1101
# -----------------
# A&b = 0000 1100
# A | B = 0011 1101