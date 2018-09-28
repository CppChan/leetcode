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

class Solution1(object):#better to understand!!!!!!!!!!!!!!!
  def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
      while height[i] < height[stack[-1]]:
        h = height[stack.pop()]
        w = i - 1 - stack[-1]
        ans = max(ans, h * w)
      stack.append(i)
    return ans