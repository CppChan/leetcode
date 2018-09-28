class Solution(object):
    def two_sum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left,right]
            elif nums[left] + nums[right] < target:
                left+=1
            else:
                right-=1

