class Solution(object):
  def searchNoDuplicate(self, array, target):
    if len(array) == 0:
      return -1
    start = 0
    end = len(array)-1
    while start< end-1: #PAY ATTENTION!!!!!
      mid = (start+end)/2
      if target == array[mid]:
        return mid
      if array[mid]>=array[start]: #PAY ATTENTION!!!!
        if target<array[mid] and target>=array[start]:
          end = mid-1
        else:
          start = mid+1
      elif array[mid]<array[start]:
        if target>array[mid] and target<=array[end]:
          start = mid+1
        else:
          end = mid-1
    if array[start]==target:
      return start
    if array[end]==target:
      return end
    return -1

  def searchWithDuplicate(self, array, target):
    if len(array) == 0:
      return -1
    start = 0
    end = len(array)-1
    while start< end-1:
      mid = (start+end)/2
      if target == array[mid]:
        return mid
      if array[mid]>array[start] or array[mid]>array[end]:#diff1!!!!!!!!!!
        if target<array[mid] and target>=array[start]:
          end = mid-1
        else:
          start = mid+1
      elif array[mid]<array[start] or array[mid]<array[end]:#diff2!!!!!!!
        if target>array[mid] and target<=array[end]:
          start = mid+1
        else:
          end = mid-1
      else:
        end-=1#diff3!!!!!!!!!!!!!!!!!!
    if array[start]==target:
      return start
    if array[end]==target:
      return end
    return -1