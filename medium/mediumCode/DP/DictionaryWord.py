class Solution(object):
  def canBreak(self, input, dict):
    n = len(dict)
    maxlength = 0
    for i in range(n):
      if len(dict[i])>maxlength:
        maxlength = len(dict[i])
    dp = [0]*(len(input)+1)
    dp[-1] = True
    for i in range(len(input)):
      if i == 0 and input[0:1] in dict:
        dp[0]=True
      if i<maxlength:
        for j in range(0, i+1):
          if input[i-j:i+1] in dict and dp[i-j-1]:
            dp[i] = True
      else:
        for j in range(0, maxlength+1):
          if input[i-j:i+1] in dict and dp[i-j-1]:
            dp[i] = True
    return dp[len(input)-1]

if __name__ == "__main__":
        s = Solution()
        print s.canBreak('bcdef', ['abc', 'bcd', 'def'])