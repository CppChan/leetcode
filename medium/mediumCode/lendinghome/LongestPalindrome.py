class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) == 0: return ''
        s, pre= s.lower(),s
        dp = [[False] * len(s) for i in range(len(s))]
        res, start = '', float('inf')
        for k in range(len(s)):
            for i in range(len(s) - k):
                j = i + k
                if i == j:dp[i][j] = True
                elif j - i == 1 and (s[j] == s[i] or s[i]==" " or s[j] == " "):dp[i][j] = True
                else:
                    if s[i]==" ": dp[i][j] = dp[i+1][j]
                    elif s[j]==" ":dp[i][j] = dp[i][j-1]
                    elif s[i] == s[j] and dp[i + 1][j - 1] == True:dp[i][j] = True
                    else:dp[i][j] = False
                if dp[i][j] and j - i + 1>1 and j - i + 1 == len(res) and i<start: res, start= pre[i:j + 1], i
                if dp[i][j] and j - i + 1>1 and j - i + 1>len(res): res, start= pre[i:j + 1], i
        return res

if __name__ == "__main__":
    s = Solution()
    print "*"+s.longestPalindrome('I went to Nurses run yesterday')+"*"