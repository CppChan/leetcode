#O(n)
class Solution(object):
    def missingNumber(self, nums):
        nums.append(-1)
        i = 0
        while i < len(nums):
            if nums[i] != -1:
                while nums[i] != i:
                    if nums[i] == -1: break
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            i += 1
        i = 0
        while i < len(nums):
            if nums[i] != i: return i
            i += 1


# sort + binary search

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        i, j = 0, len(nums)-1
        while i<j-1:
            mid = (i+j)/2
            if nums[mid]==mid:i = mid
            else:j = mid
        if nums[i]==i+1: return i
        elif j == nums[j]:return j+1
        else:return j