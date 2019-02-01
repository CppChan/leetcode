
# Given a non-empty array of integers, return the k most frequent elements.

# method 1 using max stack, complexity O( (n-k)logk)

# method 2 Bucket sort
from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
    	dic, mostfrequent = defaultdict(lambda: 0),0
    	for i in range(len(nums)):
    		dic[nums[i]]+=1
    		if dic[nums[i]]>mostfrequent: mostfrequent = dic[nums[i]]
    	freqlist = [[] for i in range(mostfrequent+2)] # get a frequency list
    	dic = dic.items()
    	for i in range(len(dic)):
    		freqlist[dic[i][1]].append(dic[i][0]) # add unique element into bucket
    	res = []
    	for i in range(len(freqlist)-1, -1, -1):
    		if len(freqlist[i])<k:
    			res.extend(freqlist[i])
    			k-=len(freqlist[i])
    		else:
    			res.extend(freqlist[i][:k+1])
    			break
    	return res