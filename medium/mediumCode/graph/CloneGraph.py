from collections import deque
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    dic = {}

    def cloneGraph(self, graph):#DFS
        if not graph: return None
        root = UndirectedGraphNode(graph.label)
        pastby = {root.label: root}
        self.dfs(graph, root, pastby)
        return root

    def dfs(self, graph, root, pastby):
        for child in graph.neighbors:
            if pastby.has_key(child.label):
                root.neighbors.append(pastby[child.label])
                continue
            new = UndirectedGraphNode(child.label)
            root.neighbors.append(new)
            pastby[child.label] = new
            self.dfs(child, new, pastby)

    def cloneGraph(self, graph):#BFS
        if not graph: return None
        root = UndirectedGraphNode(graph.label)
        queue, pastby = deque([graph]), {root.label: root}
        self.bfs(queue, root, graph, pastby)
        return root

    def bfs(self, queue, root, graph, pastby):
        while len(queue) > 0:
            item = queue.popleft()
            for child in item.neighbors:
                if child.label in pastby:
                    pastby[item.label].neighbors.append(pastby[child.label])
                    continue
                newnode = UndirectedGraphNode(child.label)
                pastby[item.label].neighbors.append(newnode)
                pastby[newnode.label] = newnode
                queue.append(child)

if __name__=='__main__':

    g = UndirectedGraphNode(-1)
    q = UndirectedGraphNode(1)
    k = UndirectedGraphNode(2)
    k.neighbors.append(g)
    g.neighbors.append(q)
    g.neighbors.append(k)
    s = Solution()
    s.cloneGraph(g)