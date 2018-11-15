class Solution(object):
    def threeSumClosest(self, num, target):
        num.sort()
        res = float('inf')
        for i in range(len(num)-2):
            start,end = i+1, len(num)-1
            while start<end:
                all = num[i]+num[start]+num[end]
                if abs(all-target)<abs(res-target): res = all
                if all == target:return res
                if all<target: start+=1
                else: end-=1
        return res

# two sum closest follow up 




# class Solution(object):
#   def threeSumClosest(self, num, target):
#     num.sort()
#     res = float('inf')
#     if not num or len(num)<3:return 0
#     for i in range(len(num)):
#         temp = target-num[i]
#         tempsum = self.find(num[0:i]+num[i+1:len(num)], temp)+num[i]
#         if abs(tempsum-target)<abs(res-target):res = tempsum
#     return res
#
#   def find(self, list, target):
#     i, j = 0, len(list)-1
#     res = float('inf')
#     while i<j:
#         if abs((list[i]+list[j])-target)<abs(res-target):res = list[i]+list[j]
#         if list[i]+list[j]<target:i+=1
#         elif list[i]+list[j]>target:j-=1
#         else:break
#     return res