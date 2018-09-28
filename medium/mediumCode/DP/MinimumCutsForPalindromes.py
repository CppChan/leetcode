class Solution(object):
    def minCuts(self, input):
        if len(input) == 0 or len(input) == 1: return 0#corner case !!
        dp = [0] * len(input)
        res = float('inf')
        for i in range(1, len(dp)):
            nowmax = float('inf')
            for j in range(i, -1, -1):
                if self.isP(input[j:i + 1]):
                    if j == 0:#corner case payattention
                        nowmax = 0
                    elif 1 + dp[j - 1] < nowmax:
                        nowmax = 1 + dp[j - 1]
            dp[i] = nowmax
        return dp[-1]

    def isP(self, array):
        i, j = 0, len(array) - 1
        while i < j:
            if array[i] != array[j]: return False
            i += 1
            j -= 1
        return True