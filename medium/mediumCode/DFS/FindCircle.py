class Solution(object):
    def findCircleNum(self, M):
        visited, count = [0] * len(M), 0
        for i in range(len(M)):
            if not visited[i]:
                self.dfs(M, i, visited)
                count += 1
        return count

    def dfs(self, M, i, visited):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(M, j, visited)