class Solution(object):
  def minJump(self, array):
      dp,nearest = [-1]*len(array),len(array)
      for i in range(len(array)-1, -1, -1):
          if nearest-i<=array[i]:
              nearest = i
              if i+array[i]>=len(array):
                  dp[i]=1
                  continue
              temp = float('inf')
              for j in range(nearest, nearest+array[i]+1):
                  if j<len(array) and dp[j]!=-1: temp=min(temp, dp[j]+1)
              dp[i]=temp
          else:
              dp[i]=-1
      return dp[0]

if __name__ == "__main__":
    s = Solution()
    print s.minJump([1, 2, 0])