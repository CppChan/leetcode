#using bucket
class Solution(object):
  def containsNearbyAlmostDuplicate(self, nums, k, t):
  	if k<1 or t<0:return False
  	dic = {}
  	for i in range(len(nums)):
  		val = nums[i]+2147483649
  		key = (nums[i]+2147483649)/(t+1)# if t == 3, then 0, 3 will go into same bucket when using t+1
  		if dic.has_key(key) or (dic.has_key(key-1) and val-dic.get(key-1)<=t) or (dic.has_key(key+1) and dic.get(key+1)-val<=t):return True
  		if len(dic)>=k:
  			dic.__delitem__((nums[i-k]+2147483649)/(t+1))
  		dic[key]=val
  	return False


#https://leetcode.com/problems/contains-duplicate-iii/description/