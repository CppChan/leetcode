class Solution(object):
  def find(self, input):
  	if len(input)==0:return 0
  	res, ret= [],0
  	self.dfs(input, res, 0,0, float('inf'))
  	for i in res:
  		ret = max(i, ret)
  	return ret

  def dfs(self, input, res,i,j, step):
  	if i<len(input) and j<len(input[0]) and input[i][j]<step:step = input[i][j]
  	if i==len(input)-1 and j == len(input[0])-1:
  		res.append(step)
  		return
  	if i<len(input)-1: self.dfs(input, res, i+1, j, step)
  	if j<len(input[0])-1: self.dfs(input, res, i, j+1, step)


# or use dp
# public static int maximumMinimumPath(int[][] matrix) {
#                 if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
#                         return 0;
#                 }
#                 int n = matrix.length;
#                 int m = matrix[0].length;
#                 int[][] dp = new int[n][m];
#                 dp[0][0] = matrix[0][0];
#                 for (int i = 1; i < n; i++) {
#                         dp[i][0] = Math.min(dp[i - 1][0], matrix[i][0]);
#                 }
#                 for (int i = 1; i < m; i++) {
#                         dp[0][i] = Math.min(dp[0][i - 1], matrix[0][i]);
#                 }
#                 for (int i = 1; i < n; i++) {
#                         for (int j = 1; j < m; j++) {
#                                 dp[i][j] = Math.min(Math.max(dp[i - 1][j], dp[i][j - 1])  # every dp point is the maximumMinimun point from start to here
#                                                 matrix[i][j]);
#                         }
#                 }
#                 return dp[n - 1][m - 1];
#         }


if __name__ == "__main__":
    s = Solution()
    print s.find([[8,4,7],[6,5,9],[4,8,10]])