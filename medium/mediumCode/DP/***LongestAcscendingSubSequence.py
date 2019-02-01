def lengthOfLIS(self, array):
    if len(array) == 0: return 0
    lenlist = [array[0]]
    for i in range(1, len(array)):
        j, k = 0, len(lenlist) - 1
        while j < k:
            mid = (j + k) / 2
            if lenlist[mid] >= array[i]:
                k = mid
            elif lenlist[mid] < array[i]:
                j = mid + 1
        if array[i] < lenlist[j]:
            lenlist[j] = array[i]
        elif array[i] > lenlist[j]:
            lenlist.append(array[i])
    return len(lenlist)

class Solution(object):
  def longest(self, array):
  	if len(array)==0:return 0
  	last_element=[array[0]]
  	for i in range(1,len(array)):
  		start,end,equal= 0,len(last_element)-1,False
  		while start<end:
  			mid = (start+end)/2
  			if last_element[mid]>array[i]:end = mid
  			elif last_element[mid]<array[i]:start = mid+1
  			else:
  				equal = True
  				break
  		if equal:continue
  		if last_element[end]>array[i]:last_element[end]=array[i]
  		elif last_element[end]<array[i]:last_element.append(array[i])
  	return len(last_element)

# For this list, we can have LIS with different length.
# For length = 1, [1], [3], [5], [2], [8], [4], [6], we pick the one with smallest tail element as the representation of length=1, which is [1]
# For length = 2, [1,2] [1,3] [3,5] [2,8], ...., we pick [1,2] as the representation of length=2.
# Similarly, we can derive the sequence for length=3 and length=4
# The result sequence would be:
# len=1: [1]
# len=2: [1,2]
# len=3: [1,3,4]
# len=4: [1,3,5,6]
#
# According to the logic in the post,we can conclude that:
# (1) If there comes another element, 9
# We iterate all the sequences, found 9 is even greater than the tail of len=4 sequence, we then copy len=4 sequence to be a new sequece, and append 9 to the new sequence, which is len=5: [1,3,5,6,9]
# The result is:
# len=1: [1]
# len=2: [1,2]
# len=3: [1,3,4]
# len=4: [1,3,5,6]
# len=5: [1,3,5,6,9]
#
# (2) If there comes another 3,
# We found len=3 [1,3,4], whose tailer is just greater than 3, we update the len=3 sequence tobe [1,3,3]. The result is:
# len=1: [1]
# len=2: [1,2]
# len=3: [1,3,3]
# len=4: [1,3,5,6]
# do binary seach in 1,2,3,6
#
# (3) If there comes another 0,
# 0 is smaller than the tail in len=1 sequence, so we update the len=1 sequence. The result is:
# len=1: [0]
# len=2: [1,2]
# len=3: [1,3,3]
# len=4: [1,3,5,6]

# follow up: longest Bitonic Sequence
class Solution(object):
  def longestBitonic(self, array):
  	if len(array)==0:return 0
  	res = 0
  	for i in range(len(array)+1):
  		if i == 0: temp = self.find(array[len(array)-1:-1:-1])
  		elif i == len(array):temp = self.find(array)
  		else:temp = self.find(array[0:i])+self.find(array[len(array)-1:i-1:-1])
  		if temp>res: res = temp
  	return res

  def find(self, nums):
    if len(nums)==0:return 0
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

#follow up Least Moves To Ascending Array

class Solution(object):
  def leastMoves(self, array):
  	if len(array)<2: return 0
  	return len(array)-self.lengthOfLIS(array)




#explaination at comment:https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation?page=2r