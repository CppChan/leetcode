class Solution(object):
    def longestPalindromeSubseq(self, s):
        if not s or len(s)==0: return ''
        dp = [[0]*len(s) for i in range(len(s))]
        res = ''
        for k in range(len(s)):
            for i in range(len(s)-k):
                j = i+k
                if i==j:dp[i][j]=1
                elif i+1==j:
                    if s[i]==s[j]: dp[i][j]=2
                    else: dp[i][j]=1
                else:
                    if s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
                    else:dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]