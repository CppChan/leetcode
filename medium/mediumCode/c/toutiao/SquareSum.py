from collections import defaultdict
class Solution(object):
    def solve(self, input):
        dic = defaultdict(lambda: 0)
        for i in range(len(input)):
            dic[abs(input[i])] += 1
        dict, res = dic.items(), set([])
        for i in range(len(dict)):
            if dict[i][1] > 1: res.add(2 * dict[i][0] * dict[i][0])
            for j in range(i + 1, len(dict)):
                res.add(dict[i][0] * dict[i][0] + dict[j][0] * dict[j][0])
        return list(res)


if __name__=="__main__":
    s = Solution()
    print s.solve([-4,-2,1,2,3,4])