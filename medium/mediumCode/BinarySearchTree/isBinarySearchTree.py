class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1(object):
    def ifBinarySearch(self, root):
        if not root:
            return True
        list = []
        self.inorder(root, list)
        for i in range(len(list) - 1):
            if list[i + 1] <= list[i]:
                return False
        return True

    def inorder(self, root, list):
        if root.left:
            self.inorder(root.left,list)
        list.append(root.val)
        if root.right:
            self.inorder(root.right,list)

class Solution2(object):
    def ifBinarySearch(self, root):
        if not root:
            return True
        return self.validate(root, -float('inf'), float('inf'))

    def validate(self, root, min, max):
        if not root:
            return True
        if root.val<=min or root.val>=max:
            return False
        return self.validate(root.left, min, root.val) and self.validate(root.right, root.val, max)


if __name__ == "__main__":
    s = Solution1()
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(8)
    d = TreeNode(1)
    e = TreeNode(4)
    f = TreeNode(6)
    g = TreeNode(9)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    print s.ifBinarySearch(a)