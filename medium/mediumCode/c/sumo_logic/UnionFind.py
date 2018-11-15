class Solution(object):
    class Union(object):

        def __init__(self, n):
            self.parent, self.rank = [i for i in range(n)], [0] * n
            self.count = n

        def find(self, node):  # this can synchronized/update a node's newest root node
            if self.parent[node] != node: self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

        def union(self, x, y):
            x_root, y_root = self.find(x), self.find(y) # have update their newest root
            if x_root == y_root: return False # loop detect
            if self.rank[x_root] > self.rank[y_root]: # y's root is lower rank
                self.parent[y_root] = x_root # son node's root will update in next find function
            elif self.rank[x_root] < self.rank[y_root]:# x's root is lower rank
                self.parent[x_root] = y_root
            else:
                self.parent[x_root] = y_root
                self.rank[y_root] += 1
            self.count -= 1
            return True

    def validTree(self, n, edges):
        u = self.Union(n)
        for i in range(len(edges)):
            x, y = edges[i][0], edges[i][1]
            if not u.union(x, y): return False
        return u.count == 1