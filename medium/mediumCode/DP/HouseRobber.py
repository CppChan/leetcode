class Solution(object):
  def rob(self, root):
    if not root: return 0
    res = self.find(root)
    return max(res[0], res[1])

  def find(self, root):
    if not root: return (0,0)
    left = self.find(root.left)
    right = self.find(root.right)
    first = root.val+left[1]+right[1]
    second = max(left[0], left[1])+max(right[0],right[1])
    return (first, second)