from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution(object):
    def solve(self, root):
        result = []
        queue = deque([])
        if not root:
            return result
        print self.findMax(queue, result, root)


    def findMax(self, queue, result, root):
        queue.append(root)
        size = len(queue)
        max = 0
        while size > 0:
            for i in xrange(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.val>max:
                    max = node.val
            size = len(queue)
            result.append(max)
            max = 0
        return result


if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(4)
    c = TreeNode(3)
    d = TreeNode(2)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    s.solve(a)


