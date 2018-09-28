class Solution(object):
  def shiftPosition(self, array):
    if len(array) == 0:
      return -1
    start = 0
    end = len(array)-1
    while start< end-1:
      mid = (start+end)/2
      if array[mid]<array[start]:
        end = mid
      elif array[mid]>array[end]:
        start = mid
      else:#PAY ATTENTION!!!!
        return 0
    if array[start]<array[end]:#PAY ATTENTION!!!!!
      	return 0
    return end