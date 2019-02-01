from collections import defaultdict


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        dic, highest = defaultdict(lambda: []), [0]
        for i in range(len(nestedList)):
            self.findlevel(nestedList[i], dic, 1, highest)
        item, res = dic.items(), 0
        for i in range(len(item)):
            member, level = item[i][1], item[i][0]
            for j in member:
                res += (highest[0] + 1 - level) * j
        return res

    def findlevel(self, nestedList, dic, level, highest):
        if nestedList.isInteger():
            if level > highest[0]: highest[0] = level
            dic[level].append(nestedList.getInteger())
        else:

            nList = nestedList.getList()
            for i in range(len(nList)):
                self.findlevel(nList[i], dic, level + 1, highest)