class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findminHeight(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = float('inf')
        right = float('inf')
        if root.left:
            left = self.findminHeight(root.left)
        if root.right:
            right = self.findminHeight(root.right)
        return min(left, right)+1

if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(8)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    d.left = g
    result = s.findminHeight(a)
    print result