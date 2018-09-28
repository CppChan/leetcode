class Solution(object):
  def largestSum(self, array):
    dp = [[0]*3 for i in range(len(array))]
    res = [array[0],0,0]
    for i in range(len(array)):
        if i == 0:dp[i]=[array[0],0,0]
        else:
            if dp[i-1][0]<0: dp[i]=[array[i],i,i]
            else: dp[i]=[dp[i-1][0]+array[i], dp[i-1][1],i]
        if dp[i][0]>res[0]: res = dp[i]
    return res