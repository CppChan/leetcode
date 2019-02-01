class Solution(object):
    def maxValue(self, n, m, max_t, beauty, u, v, t):
        place = []
        for i in range(n):
            place.append({})
        for i in range(len(u)):
            place[u[i]][v[i]] = t[i]
            place[v[i]][u[i]] = t[i]
        res, visited = [0], set([0])
        self.dfs(place, visited, res, beauty[0], 0, 0, max_t, beauty)
        return res[0]

    def dfs(self, place, visited, res, cur_val, cur_point, time, max_t, beauty):
        if cur_point == 0 and time < max_t and time > 0:
            res[0] = max(res[0], cur_val)
        dest = place[cur_point].items()
        for i in range(len(dest)):
            if time + dest[i][1] > max_t: continue
            ifvisited = False
            if dest[i][0] not in visited:
                ifvisited = True
                visited.add(dest[i][0])
                cur_val += beauty[dest[i][0]]
            self.dfs(place, visited, res, cur_val, dest[i][0], time + dest[i][1], max_t, beauty)
            if ifvisited:
                visited.remove(dest[i][0])
                cur_val -= beauty[dest[i][0]]
s = Solution()
print s.maxValue(5,6,70,[30,80,100,50,50],[4,1,0,4,2,2],[3, 4, 3, 0, 3, 0],[20, 15, 40, 10, 100, 10])
print s.maxValue(4,3,49,[0,32,10,43],[0,2,0],[1,0,3],[10,13,17])
print s.maxValue(4,3,30,[5,10,15,20],[0,1,0,1],[1,2,3,3],[6,6,10,1])
