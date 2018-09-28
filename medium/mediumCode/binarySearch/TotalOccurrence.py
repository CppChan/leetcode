class Solution(object):
  def totalOccurrence(self, array, target):
    if not array:
      return 0
    start=0
    end = len(array)-1
    place = -float('inf')
    while start<end-1:
      mid = (start+end)/2
      if array[mid]==target:
        place = mid
        break
      if array[mid]<target:
        start = mid+1
      elif array[mid]>target:
        end = mid-1
    if array[start]==target:
      place = start
    elif array[end]==target:
      place = end
    if place<0:
      return 0
    left, right = place, place
    res = 1
    while True:##!!!!!!!!!!!!!
      leftnext, rightnext = False, False
      if left-1>=0 and array[left-1]==target:
        left -=1
        res+=1
        leftnext = True
      if right+1<len(array) and array[right+1]==target:
        right+=1
        res+=1
        rightnext = True
      if leftnext == False and rightnext == False:
        break
    return res