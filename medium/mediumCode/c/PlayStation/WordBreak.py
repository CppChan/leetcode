class Solution(object):
    def wordBreak(self, s, wordDict):
        if len(s) == 0 or len(wordDict) == 0: return []
        longest = 0
        lenset = []
        for word in wordDict:
            lenset.append(len(word))
            longest = max(longest, len(word))
        lenset = sorted(list(set(lenset)))
        wordDict = set(wordDict)
        res = []
        self.dfs(res, "", wordDict, longest, 0, s, lenset)
        return res

    def dfs(self, res, temp, wordDict, longest, start, s, lenset):
        if start == len(s):
            res.append(temp[1:])
            return
        for length in lenset:
            if start + length > len(s): break
            if s[start: start + length] in wordDict:
                self.dfs(res, temp + " " + s[start:start + length], wordDict, longest, start + length, s, lenset)

s = Solution()
print s.wordBreak("pineapplepenapple",["apple","pen","applepen","pine","pineapple"])