class segmentTreeNode(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None

class segmentTree(object):
    def __init__(self, array):
        self.array = array
        self.root = self.buildSegmentTree(array, 0, len(array)-1)

    def buildSegmentTree(self, array, start, end):
        if start>end:
            return None
        if start == end:
            cur = segmentTreeNode(start, end)
            cur.sum = array[start]
            return cur
        else:
            mid = (start+end)/2
            cur = segmentTreeNode(start, end)
            cur.left = self.buildSegmentTree(array, start, mid)
            cur.right = self.buildSegmentTree(array, mid, end)
            if cur.left:
                cur.sum+=cur.left.sum
            if cur.right:
                cur.sum+=cur.right.sum
            return cur

    def update(self, index, val):
        diff = val-self.array[index]
        self.array[index]= val
        cur = self.root
        while cur:
            cur.sum+=diff
            if index>=cur.left.start and index<=cur.left.end:
                cur = cur.left
            else:
                cur = cur.right

    def sum(self, start, end):
        return self.getsum(self, self.root, start, end)

    def getsum(self, root, start, end):
        if not root or root.start>end or root.end<start:
            return 0
        if root.start>=start and root.end<=end:
            return root.sum
        else:
            return self.getnum(root.left, start,end)+self.getnum(root.right, start, end)
