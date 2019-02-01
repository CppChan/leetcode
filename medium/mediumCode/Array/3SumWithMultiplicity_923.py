from collections import defaultdict


class Solution(object):
    def threeSumMulti(self, A, target):
        A.sort()
        res = 0
        for i in range(len(A) - 2):
            if A[i] > target / 3: break
            res += self.twoSum(A, i + 1, target - A[i])
        return res % (10 ** 9 + 7)

    def twoSum(self, nums, i, target):
        res = 0
        visited = defaultdict(lambda: 0)
        while i < len(nums):
            if nums[i] in visited:
                res += visited[nums[i]]
            if nums[i] <= target / 2: visited[target - nums[i]] += 1
            i += 1
        return res

s =Solution()
print s.threeSumMulti([1,1,2,2,2,2],5)