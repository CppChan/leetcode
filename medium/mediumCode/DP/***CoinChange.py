#无限硬币，有多少种方法

#best
class Solution(object):
    def change(self,  amount,coins):
        dp = [0]*(amount+1) # 注意amount+1！！！！ 面试的时候错过
        dp[0]=1
        for coin in coins: # only use this coin and this coin before
            for i in range(coin, len(dp)):
                dp[i]+=dp[i-coin]
        return dp[-1]

    # 两个for循环不要搞反了
    # 如果dp的loop在前面，会出现 9 = 252， 9=225两种情况重复都算了

#second

class Solution(object):
    def change(self, amount, coins):
        dp = [[0] * (amount + 1) for i in range(len(coins) + 1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j == 0:dp[i][j] = 1
                elif i == 0:dp[i][j] = 0
                else:
                    if coins[i - 1] > j:dp[i][j] = dp[i - 1][j]
                    else:dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
        return dp[-1][-1]


#无限硬币，最少几个, 类似
# public int coinChange(int[] coins, int amount) {
#     if (amount < 1) return 0;
#     int[] dp = new int[amount + 1];
#     Arrays.fill(dp, Integer.MAX_VALUE);
#     dp[0] = 0;
#     for (int coin : coins) {
#         for (int i = coin; i <= amount; i++) {
#             if (dp[i - coin] != Integer.MAX_VALUE) {
#                 dp[i] = Math.min(dp[i], dp[i - coin] + 1);
#             }
#         }
#     }
#     return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
# }





class Solution(object):
    def coinChange(self, coins, amount):
