class Solution(object):
  def minCost(self, cuts, length):
    if length<=1:
      return 0
    return self.cutwood(0, length, cuts)

  def cutwood(self, left, right, cuts):
    if len(cuts) == 0 :
      return 0
    conti = False
    for k in cuts:
        if k>left and k<right:
            break
        if k == cuts[-1] and  not (k>left and k<right):
            return 0
    min = float('inf')
    for i in range(len(cuts)):
        if cuts[i] > left and cuts[i] < right:
            temp = cuts[i]
            cuts.pop(i)
            tempcost = self.cutwood(left, temp, cuts) + self.cutwood(temp, right, cuts) + (right - left)
            if tempcost < min:
                min = tempcost
            cuts.insert(i, temp)
    return min

if __name__ == "__main__":
        s = Solution()
        print s.minCost([2,4,9,10], 12)