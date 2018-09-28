class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tuple(object):
    def __init__(self):
        self.root = None
        self.mindif = -1

class Tuple2(object):
    def __init__(self):
        self.root = None
        self.mindif = -1
        self.height = 0
    def __init__(self, root1, mindif1, height1):
        self.root = root1
        self.mindif = mindif1
        self.height = height1

class solution(object):
    def findminDiff(self, root, tup):#work
        if not root:
            return 0
        leftHeight = self.findminDiff(root.left, tup)
        rightHeight = self.findminDiff(root.right, tup)
        if(abs(leftHeight-rightHeight)>tup.mindif):
            tup.mindif = abs(leftHeight-rightHeight)
            tup.root = root
        return leftHeight + rightHeight+1

    def findminDiff2(self, root):#work
        if not root:
            return Tuple2(None, -1, 0)
        leftTuple = self.findminDiff2(root.left)
        rightTuple = self.findminDiff2(root.right)
        if(abs(leftTuple.height-rightTuple.height)>leftTuple.mindif and abs(leftTuple.height-rightTuple.height)>rightTuple.mindif):
            return Tuple2(root, abs(leftTuple.height-rightTuple.height),leftTuple.height+rightTuple.height+1)
        else:
            if(leftTuple.mindif>rightTuple.mindif):
                return Tuple2(leftTuple.root, leftTuple.mindif, leftTuple.height+rightTuple.height+1)
            else:
                return Tuple2(rightTuple.root, rightTuple.mindif, leftTuple.height+rightTuple.height+1)

    def findminDiff3(self, root, maxDiff, res):#do not work
        if not root:
            return 0
        left_total = self.findminDiff3(root.left, maxDiff, res)
        right_total = self.findminDiff3(root.right, maxDiff, res)
        if(abs(left_total-right_total)>maxDiff):
            maxDiff = abs(left_total-right_total)
            res = root # cannont do that, because res refer to a new TreeNode, we can use findminDiff1's tuple
        return left_total+right_total+1



if __name__ == "__main__":
    tup = Tuple2(None, -1, 0)
    s = solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(8)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    h = TreeNode(9)
    i = TreeNode(10)
    a.left = b
    a.right = c
    b.left = d
    # b.right = e
    c.left = f
    d.left = g
    g.left = h
    c.right = i
    # t = s.findminDiff2(a)
    # print t.mindif
    res = TreeNode(100)
    maxDiff = -1
    s.findminDiff3(a, maxDiff, None)
    print maxDiff
