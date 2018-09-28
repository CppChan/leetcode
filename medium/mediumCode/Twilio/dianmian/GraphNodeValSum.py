class Node:
    def __init__(self, x):
        self.val = x
        self.neighbors = []


class Solution(object):
    def valSum(self, graph, input):
        if len(graph) == 0: return 0
        for root in graph:
            sum, find, isvisited = [0], [False], set([])
            self.dfs(root, input, sum, find, isvisited)
            if find[0]: return sum[0] - input
        return 0

    def dfs(self, root, input, sum, find, isvisited):
        if root in isvisited:
            return
        else:
            isvisited.add(root)
            sum[0] += root.val
        if root.val == input: find[0] = True
        for i in range(len(root.neighbors)):
            self.dfs(root.neighbors[i], input, sum, find, isvisited)

if __name__ == "__main__":
    s = Solution()
    a,b,c,d,e,f,g,h = Node(3),Node(3),Node(5),Node(2),Node(6),Node(3),Node(9),Node(11)
    a.neighbors=[b]
    b.neighbors = [c,d,e]
    d.neighbors = [b,e]
    e.neighbors = [b,d]
    f.neighbors = [g,h]
    print s.valSum([a,f],2)

