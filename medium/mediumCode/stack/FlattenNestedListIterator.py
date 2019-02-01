
#https://leetcode.com/problems/flatten-nested-list-iterator/


from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        self.list = deque(nestedList)
        self.current = []

    def next(self):
        if len(self.current) == 0:
            flatlist = []
            self.flat(self.list.popleft(), flatlist)
            self.current = flatlist
        res = self.current[0]
        self.current = self.current[1:]
        return res

    def hasNext(self):
        if len(self.current) > 0 or len(self.list) > 0: return True

    def flat(self, Integer, flatlist):
        if Integer.isInteger:
            flatlist.append(Integer.getInteger)
        else:
            Ilist = Integer.getList()
            for i in range(len(Ilist)):
                self.flat(Ilist[i], flatlist)

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False