class Solution(object):
    def nextPermutation(self, num):
        if len(num) == 0 or len(num) == 1: return num
        j = len(num) - 2
        while j >= 0:
            if num[j] < num[j + 1]:
                break
            else:
                j -= 1
        if j < 0:
            self.exchange(num, 0, len(num) - 1)
            return num
        for i in range(j + 1, len(num)):
            if num[i] < num[j]: break
        if i == len(num) - 1 and num[i] > num[j]:
            index = i
        else:
            index = i - 1
        temp = num[index]
        num[index] = num[j]
        num[j] = temp
        self.exchange(num, j + 1, len(num) - 1)
        return num

    def exchange(self, num, start, end):
        temp = 0
        while start < end:
            temp = num[end]
            num[end] = num[start]
            num[start] = temp
            start += 1
            end -= 1