class Solution(object):
  def threeSumClosest(self, num, target):
    num.sort()
    res = float('inf')
    if not num or len(num)<3:return 0
    for i in range(len(num)):
        temp = target-num[i]
        tempsum = self.find(num[0:i]+num[i+1:len(num)], temp)+num[i]
        if abs(tempsum-target)<abs(res-target):res = tempsum
    return res

  def find(self, list, target):
    i, j = 0, len(list)-1
    res = float('inf')
    while i<j:
        if abs((list[i]+list[j])-target)<abs(res-target):res = list[i]+list[j]
        if list[i]+list[j]<target:i+=1
        elif list[i]+list[j]>target:j-=1
        else:break
    return res