class Solution(object):
    def trap(self, array):
        res = 0
        if len(array) < 3: return 0
        begin = 0
        while begin < len(array) - 1 and array[begin + 1] >= array[begin]:
            begin += 1
        if begin == len(array) - 1: return 0
        i = begin
        while i < len(array) - 1:
            while i < len(array) - 1 and array[i + 1] == array[i]: i += 1#corner case!!!!
            j = i + 1
            temp = i
            while j < len(array) and array[j] <= array[j - 1]: j += 1
            if j == len(array): break
            temp = j
            while j < len(array):
                if array[j] > array[temp]: temp = j#corner case!!!!
                if array[j] >= array[i]: break#corner case!!!!
                j += 1
            j = temp
            if array[j] >= array[i]:
                while j < len(array) - 1 and array[j + 1] >= array[j]: j += 1#corner case!!!!
            res += self.compute(array, i, j)
            i = j
        return res

    def compute(self, array, start, end):
        res = 0
        if array[start] <= array[end]:
            i = start + 1
            while array[i] < array[start]:
                res += (array[start] - array[i])
                i += 1
            return res
        elif array[start] > array[end]:
            i = end - 1
            while array[i] < array[end]:
                res += (array[end] - array[i])
                i -= 1
            return res