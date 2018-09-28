class Solution(object):
  def sumToTarget(self, array, target):
  	dic = {}
  	temp = 0
  	if target == 0:
  		list = set([])
  		for i in range(len(array)):
  			temp+=array[i]
  			if temp == target:return True
  			if temp in list: return True
  			else: list.add(temp)
  		return False
  	for i in range(len(array)):
  		temp+=array[i]
  		if temp==target: return True
  		a = temp/target
  		b = temp%target
  		if dic.has_key(b):
  			for item in dic[b]:
  				if a-item==1:return True
  			dic[b].append(a)
  		else:
  			dic[b]=[a]
  	return False


#follow up Largest subarray with equal number of 0s and 1s

class Solution2(object):
  def longest(self, array):
  	for i in range(len(array)):
  		if array[i]==0: array[i]=-1
  	prefix = [0]*len(array)
  	temp = 0
  	for i in range(len(prefix)):
  		temp+=array[i]
  		prefix[i] = temp
  	dic = {}
  	res = 0
  	for i in range(len(prefix)):
  		if prefix[i]==0 and i+1>res:res = i+1
  		elif dic.has_key(prefix[i]):
  			temp = i-dic[prefix[i]]
  			if temp>res:res = temp
  		else:
  			dic[prefix[i]]=i
  	return res

#For sum to multiple of  k

# public boolean checkSubarraySum(int[] nums, int k) {
#     Map<Integer, Integer> map = new HashMap<Integer, Integer>(){{put(0,-1);}};;
#     int runningSum = 0;
#     for (int i=0;i<nums.length;i++) {
#         runningSum += nums[i];
#         if (k != 0) runningSum %= k;
#         Integer prev = map.get(runningSum);
#         if (prev != null) {
#             if (i - prev > 1) return true;
#         }
#         else map.put(runningSum, i);
#     }
#     return false;
# }