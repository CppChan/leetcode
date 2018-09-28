class Solution(object):
  def getNextPermutation(self, nums):
  	newnums = []
  	for i in range(len(nums)):
  		newnums.append(nums[i])
  	nums = newnums
  	if len(nums)==1:return "BIGGEST"
  	smallest,stop = nums[-1],0
  	for i in range(len(nums)-2, -1, -1):
  		if int(nums[i])<int(nums[i+1]):
  			stop = i
  			break
  	if stop==0 and nums[0]>=nums[1]:return "BIGGEST"
  	for i in range(len(nums)-1, stop, -1):
  		if int(nums[i])>int(nums[stop]):
  			temp = nums[i]
  			nums[i]=nums[stop]
  			nums[stop]=temp
  			break
  	back = nums[stop+1:len(nums)]
  	res =nums[0: stop+1]
  	for i in range(len(back)-1, -1, -1):
  		res+=back[i]
  	return "".join(res)
if __name__=="__main__":
    s = Solution()
    s.getNextPermutation("279134399742")