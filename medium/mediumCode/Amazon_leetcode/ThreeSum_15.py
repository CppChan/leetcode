class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if nums[i] > 0: break
            three_sum = self.twoSum(nums, i + 1, nums[i], 0 - nums[i])
            if len(three_sum) > 0: res.extend(three_sum)
        return res

    def twoSum(self, nums, i, first, target):
        res = []
        visited = set([])
        j = i
        while i < len(nums):
            if nums[i] in visited:
                res.append([first, target - nums[i], nums[i]])
                visited.remove(nums[i])
            elif nums[i] <= target / 2 and (i == j or nums[i] != nums[i - 1]):
                # situation when target = 4, list = [2,2,2,2...]
                # if i = j, means the first element, we must add it into the set
                visited.add(target - nums[i])
            i += 1
        return res