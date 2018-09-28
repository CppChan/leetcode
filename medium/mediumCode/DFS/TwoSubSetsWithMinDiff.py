class Solution(object):
    def minDifference(self, array):
        sum = 0
        for i in array:
            sum += i
        mid = sum / 2
        if len(array) % 2 == 0:
            res = [float('inf')]
            self.findSet(res, 0, array, mid, len(array) / 2)
            return abs(mid + res[0] - (sum - (mid + res[0])))
        else:
            res1 = [float('inf')]
            self.findSet(res1, 0, array, mid, len(array) / 2)
            res2 = [float('inf')]
            self.findSet(res2, 0, array, mid, len(array) / 2 + 1)
            return min(abs(mid + res1[0] - (sum - (mid + res1[0]))), abs(mid + res2[0] - (sum - (mid + res2[0]))))

    def findSet(self, res, now, array, mid, size):
        if size == 0:
            if abs(now - mid) < abs(res[0]):
                res[0] = now - mid
            return
        for i in range(len(array)):
            temp = array[i]
            array.pop(i)
            self.findSet(res, now + temp, array, mid, size - 1)
            array.insert(i, temp)


if __name__ == "__main__":
    s =Solution()
    print s.minDifference([3,1,2,5])