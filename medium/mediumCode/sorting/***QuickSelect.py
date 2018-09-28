class Solution(object):
  def findKthLargest(self, nums, k):
  	if k == 0:return 0
  	start, end, i, j, key= 0, len(nums)-1, 0, len(nums)-1, nums[0]
  	while i < j:
  		while i<j and key<=nums[j]:#<=, ow will dead recursion
  			j-=1
  		temp = nums[j]
  		nums[j]=key
  		nums[i] = temp
  		while i<j and key>=nums[i]:
  			i+=1
  		temp = nums[i]
  		nums[i]=key
  		nums[j] = temp
  	if end-i+1==k:return nums[i]
  	elif end-i+1>k: return self.findKthLargest(nums[i+1:len(nums)], k)
  	else: return self.findKthLargest(nums[0:i], k-(end-i+1))

if __name__=="__main__":
    s = Solution()
    s.findKthLargest([7,6,5,4,3,2,1],2)