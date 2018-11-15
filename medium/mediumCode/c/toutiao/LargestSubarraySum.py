class Solution(object):
  def largestSum(self, array):
    res = array[0]
    if len(array)==0:
      return 0
    pre = [0]*len(array)
    pre[0]=array[0]
    for i in range(1,len(array)):
      if pre[i-1]<=0:
        pre[i]=array[i]
      else:
        pre[i]=pre[i-1]+array[i]
      res = max(res, pre[i])
    return res