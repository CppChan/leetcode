# dont forget to consider when array has negative value.
# otherwise can use two pointer to solve it.


# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.



from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        dic, res, prefix = defaultdict(lambda: 0),0,[]
        for i in range(len(nums)):
            if len(prefix)==0: prefix.append(nums[i])
            else: prefix.append(prefix[i-1]+nums[i])
            if prefix[-1]==k: res+=1 # dont forget!!!!
            if prefix[-1] in dic: res += dic[prefix[-1]]
            dic[prefix[-1]+k]+=1
        return res


