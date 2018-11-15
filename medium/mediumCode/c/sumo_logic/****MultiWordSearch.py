class Solution(object):
    def findWords(self, matrix, cand):
        if len(cand) == 0 or len(matrix) == 0: return []
        trie, res = {}, []
        for w in cand:
            t = trie
            for l in w:
                if l not in t: t[l] = {}
                t = t[l]
            t['#'] = '#'#the word end here
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                t = trie
                self.dfs(matrix, i, j, t, res, "")
        return list(set(res))

    def dfs(self, matrix, i, j, t, res, temp):
        if matrix[i][j] not in t: return # no match letter
        if '#' in t[matrix[i][j]]:#last word
            res.append(temp + matrix[i][j]) # here, remember dont return ,becasue there may be word need to find continuely
        matrix[i][j] += "*"
        if i > 0: self.dfs(matrix, i - 1, j, t[matrix[i][j][:1]], res, temp + matrix[i][j][:1])
        if i < len(matrix)-1: self.dfs(matrix, i + 1, j, t[matrix[i][j][:1]], res, temp + matrix[i][j][:1])
        if j > 0: self.dfs(matrix, i, j - 1, t[matrix[i][j][:1]], res, temp + matrix[i][j][:1])
        if j < len(matrix[0])-1:self.dfs(matrix, i, j + 1, t[matrix[i][j][:1]], res, temp + matrix[i][j][:1])
        matrix[i][j] = matrix[i][j][:1]

s = Solution()
print s.findWords([["a","b"],["a","a"]],
["aba","baa","bab","aaab","aaa","aaaa","aaba"])