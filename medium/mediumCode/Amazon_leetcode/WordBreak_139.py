class Solution(object):
    def wordBreak(self, s, wordDict):
    	wordDict, dp= set(wordDict), [0]*len(s)
    	if len(s)==0: return True
    	if s[0] in wordDict: dp[0]=1
    	for i in range(1,len(s)):
    		for j in range(i,-1,-1):
    			if j == 0 and s[:i+1] in wordDict: dp[i]=1
    			else:
    				if s[j: i+1] in wordDict and dp[j-1]==1: dp[i]=1
        if dp[-1]==1:return True
        else:return False