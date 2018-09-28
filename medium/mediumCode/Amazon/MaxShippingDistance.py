class Solution():
    def maxShippingDist1(self, list1, list2, maxDist):
        res, tempmax = [], 0
        for item1 in list1:
            for item2 in list2:
                if item1[1] + item2[1] <= maxDist and item1[1] + item2[1] > tempmax:
                    res, tempmax = [[item1[0], item2[0]]], item1[1] + item2[1]
                elif item1[1] + item2[1] <= maxDist and item1[1] + item2[1] == tempmax:
                    res.append([item1[0], item2[0]])
        return res

    def maxShippingDist2(self, list1, list2, maxDist):
        if not list1 or not list1[0] or not list2 or not list2[0]: return []
        ret = []
        objectDist = 0
        for item1 in list1:
            for item2 in list2:
                if len(item1) == 2 and len(item2) == 2:
                    if item1[1] + item2[1] <= maxDist:
                        objectDist = max(objectDist, item1[1] + item2[1])
        for item1 in list1:
            for item2 in list2:
                if len(item1) == 2 and len(item2) == 2:
                    if item1[1] + item2[1] == objectDist: ret.append([item1[0], item2[0]])
        return ret

if __name__=="__main__":
    s = Solution()
    print s.maxShippingDist1([[1,3000], [2, 5000], [3, 7000], [4, 10000]], [[1,2000], [2, 3000], [3, 4000], [4, 5000]],10000)
    print s.maxShippingDist2([[1,3000], [2, 5000], [3, 7000], [4, 10000]], [[1,2000], [2, 3000], [3, 4000], [4, 5000]],10000)