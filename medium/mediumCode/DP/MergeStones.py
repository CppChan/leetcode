class Solution(object):
  def minCost(self, stones):
    if len(stones)==1:
      return 0
    if len(stones)==2:
      return stones[0]+stones[1]
    else:
      mincost = float('inf')
      for i in range(len(stones)-1):
        add = stones[i+1]
        temp = stones[i]+stones[i+1]
        stones[i] = stones[i]+stones[i+1]
        stones.pop(i+1)
        mincost = min(mincost, self.minCost(stones)+temp)
        stones[i]=stones[i]-add
        stones.insert(i+1, add)
    return mincost

