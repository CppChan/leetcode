class Solution(object):
  def longestConsecutive(self, array):
  	dic={}
  	res = 0
  	if not array: return 0
  	list1 = set(array)
  	array = list(list1)
  	for i in range(len(array)):
  		if not dic.has_key(array[i]-1) and not dic.has_key(array[i]+1):
  			dic[array[i]]=(1,array[i])
  			if 1>res: res=1
  		else:
  			if dic.has_key(array[i]-1) and dic.has_key(array[i]+1):
  				tuple1 = dic[array[i]-1]
  				tuple2 = dic[array[i]+1]
  				dic[tuple1[1]]=(tuple1[0]+tuple2[0]+1, tuple2[1])
  				dic[tuple2[1]]=(tuple1[0]+tuple2[0]+1, tuple1[1])
  				if array[i]-1!=tuple1[1]:dic.__delitem__(array[i]-1)#corner case
  				if array[i]+1!=tuple2[1]:dic.__delitem__(array[i]+1)#corner case
  				if tuple1[0]+tuple2[0]+1>res: res=tuple1[0]+tuple2[0]+1
  			elif dic.has_key(array[i]-1):
  				tuple1 = dic[array[i]-1]
  				dic[tuple1[1]]=(tuple1[0]+1, array[i])
  				dic[array[i]]=(tuple1[0]+1, tuple1[1])
  				if array[i]-1!=tuple1[1]:dic.__delitem__(array[i]-1)#corner case
  				if tuple1[0]+1>res: res = tuple1[0]+1
  			elif dic.has_key(array[i]+1):
  				tuple1 = dic[array[i]+1]
  				dic[tuple1[1]]=(tuple1[0]+1, array[i])
  				dic[array[i]]=(tuple1[0]+1, tuple1[1])
  				if array[i]+1!=tuple1[1]:dic.__delitem__(array[i]+1)#corner case
  				if tuple1[0]+1>res: res = tuple1[0]+1
  	return res

  def longestConsecutive2(self, nums): #better solution!!!!!!!
      nums = set(nums)
      best = 0
      for x in nums:
          if x - 1 not in nums:
              y = x + 1
              while y in nums:
                  y += 1
              best = max(best, y - x)
      return best