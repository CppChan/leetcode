class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):

    def changeNode(self, root):
        new = TreeNode(20)
        root = new


if __name__ == "__main__":
    a = TreeNode(2)
    b = solution()
    b.changeNode(a)
    print a.val