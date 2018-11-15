class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in range(len(nums)):
            self.dfs(res, nums, i, [nums[i]])
        return res

    def dfs(self, res, nums, i, temp):
        res.append(temp[:])
        for j in range(i + 1, len(nums)):
            temp.append(nums[j])
            self.dfs(res, nums, j, temp)
            temp.pop(-1)
