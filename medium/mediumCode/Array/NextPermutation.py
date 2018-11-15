
#begin from last element, when encounter nums[j]<nums[j+1], swap nums[j] with the first larger than nums[j] element in the behind part
#like 32431 -> 33421, then sort the behind part ->33124
class Solution(object):
    def nextPermutation(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            a = 0
        else:
            j, hasswap = len(nums) - 2, False
            while j >= 0:
                if nums[j] < nums[j + 1]:
                    for i in range(len(nums) - 1, j, -1):
                        if nums[i] > nums[j]:
                            self.swap(nums, i, j)
                            break
                    j += 1
                    hasswap = True
                if hasswap or j == 0:
                    k = len(nums) - 1
                    while j < k:
                        self.swap(nums, j, k)
                        j, k = j + 1, k - 1
                    break
                j -= 1

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp