class solution(object):

    #******using dictionary
    def find1(self, list, k):
        ans = sum = 0
        dic = {}
        for i in range(len(list)):
            if sum not in dic:
                dic[sum]=0
            dic[sum]+=1
            sum+=list[i]
            if sum-k in dic:
                ans+= dic[sum-k]
        return ans


    # using DP, fail
    def find(self, list, k):
        opt = [[0]*(k+1) for q in range(len(list))] #must use this way to initialize a 2d array
        for i in xrange(len(list)):
            for j in xrange(k+1):
                if i == 0:
                    if list[i]==j:
                        opt[i][j]=1
                    else:
                        opt[i][j]=0
                if j == 0:
                    opt[i][j] = 1
                elif i!=0 and j!=0:
                    if j>=list[i]:
                        opt[i][j]=opt[i-1][j-list[i]]+opt[i-1][k]
                    else:
                        opt[i][j]=opt[i-1][j]
        return opt[len(list)-1][k]

    # def aaa(self):
    #     b=[[0]*3 for i in range(2)]
    #     for i in range(2):
    #         for j in range(2):
    #             b[i][j] = 1

    # def uniquePathsWithObstacles(self, obstacleGrid):
    #     """
    #     :type obstacleGrid: List[List[int]]
    #     :rtype: int
    #     """
    #     m = len(obstacleGrid)
    #     n = len(obstacleGrid[0])
    #     dp = [[0] * (n + 1)] * (m + 1)
    #     dp[0][1] = 1
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if obstacleGrid[i - 1][j - 1] == 0:
    #                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #             else:
    #                 dp[i][j] = 0

        # return dp[m][n]

if __name__ == "__main__":
    s = solution()
    print s.find1([2,5,1,6,3,4,0],7)