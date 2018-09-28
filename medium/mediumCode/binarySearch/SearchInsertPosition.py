class Solution(object):
  def searchInsert(self, input, target):
    i,j=0,len(input)-1
    if len(input)==0: return 0
    if len(input)==1:
        if input[0]>=target:return 0
        else:return 1
    while i<j-1:
        mid = (i+j)/2
        if input[mid]<target: i  = mid
        elif input[mid]>=target: j = mid
    if target<=input[i]: return i
    elif target>input[j]:return j+1
    else:return j