class Solution(object):
  def getMinDrops(self, K, B):
    dp = [[0]*B for i in range(K)]#means can flow k balls for B floor building
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0:dp[i][j] = j+1
            elif j == 0: dp[i][j]=1
            else:
                temp = float('inf')
                for q in range(j+1): #if flow the ball at q floor
                    tempmax = 0
                    if q == 0: tempmax =max(1, dp[i][j-q-1])
                    elif q == j: tempmax = dp[i-1][q-1]
                    else:tempmax =max(dp[i-1][q-1], dp[i][j-q-1])
                    if tempmax<temp:temp = tempmax
                dp[i][j]=1+temp
    return dp[K-1][B-1]

if __name__ =="__main__":
    s = Solution()
    s.getMinDrops(2,5)