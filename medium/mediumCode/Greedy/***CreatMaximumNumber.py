class Solution(object):
  def maxNumber(self, nums1, nums2, k):
  	if k == 0:return[]
  	if len(nums1)+len(nums2)<k:return []
  	temp1,temp2,max1,max2= -float('inf'),-float('inf'),0,0
  	more1 = max(1,k-len(nums2))-1
  	for j in range(len(nums1)-more1):
  		if nums1[j]>temp1:temp1,max1= nums1[j],j
  	more2 = max(1,k-len(nums1))-1
  	for q in range(len(nums2)-more2):
  		if nums2[q]>temp2:temp2,max2=nums2[q],q
  	res=[max(temp1,temp2)]
  	if temp1!=temp2:#each time get a biggest one from two list
  		if res[0]==temp2:res.extend(self.maxNumber(nums1, nums2[max2+1:],k-1))
  		else:res.extend(self.maxNumber(nums1[max1+1:], nums2,k-1))
  		return res
  	else:
  		res.extend(self.compare(self.maxNumber(nums1[max1+1:],nums2,k-1),self.maxNumber(nums1,nums2[max2+1:],k-1)))
  		return res

  def compare(self, array1, array2):
  	if not array1 or not array2:return []
  	for i in range(len(array1)):
  		if array1[i]>array2[i]:return array1
  		elif array1[i]<array2[i]:return array2
  	return array1

if __name__=="__main__":
    s = Solution()
    print s.maxNumber([3, 4, 6, 5],[9, 1, 2, 5, 8, 3],3)