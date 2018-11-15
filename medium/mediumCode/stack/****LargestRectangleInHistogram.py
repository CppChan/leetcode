class Solution(object):
  def largest(self, array):
    stack = []
    res = 0
    size = len(array)
    i = 0
    while i < size+1:
      if i == size:
        h = 0
      else:
        h = array[i]
      if len(stack) == 0 or h>=array[stack[-1]]:
        stack.append(i)
      else:
        temp = stack.pop()
        if len(stack)== 0:
          res = max(res, array[temp]*i)
        else:
          res = max(res, array[temp]*(i-stack[-1]-1))
        i-=1
      i+=1
    return res
#height is an array store ascending height building's index
class Solution1(object):#better to understand!!!!!!!!!!!!!!!
  def largestRectangleArea(self, height):
    height.append(0)#dummy building, because of this dummy building,which has smallest height, all the building before it will be pop by stack, and compute area
    stack = [-1] # used for compute area of the first building
    ans = 0
    for i in xrange(len(height)):
      while height[i] < height[stack[-1]]:
        h = height[stack.pop()] #make the array ascending height
        w = i - 1 - stack[-1] # for this height, its largest width, include before building and after building
        ans = max(ans, h * w)
      stack.append(i)
    return ans

if __name__=="__main__":

  # run an example  [2,3,4,5,6]
  s = Solution1()
  print s.largestRectangleArea([2,3,4,2])