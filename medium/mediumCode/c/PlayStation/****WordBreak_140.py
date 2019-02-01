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



#method 2 so quick
class Solution(object):
    def wordBreak(self, s, wordDict):
    	return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, sbranch):
    	if s == "":return [""]
    	if s in sbranch: return sbranch[s] # sbranch means for each substring s, its future possible combination
    	res = []
    	for word in wordDict:
    		branchlist = []
    		if s.startswith(word):
    			branchlist = self.dfs(s[len(word):], wordDict, sbranch)
    		for branch in branchlist:
    			if len(branch)==0: res.append(word)#means meet the last word
    			else:res.append(word+" "+branch)
    	sbranch[s] = res
    	return res


