class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution(object):

    def lowestCommonAncestor(self, root, p, q):#sososo efficient!!!!
        if root in (None, p, q): return root
        left, right = (self.lowestCommonAncestor(kid, p, q)
                       for kid in (root.left, root.right))
        return root if left and right else left or right #if left and not right return left; if right and not left return right


    list1 = []
    def findcommon2(self, root, node1, node2):
        if(root.val == node1.val or root.val == node2.val):
            return root
        list = []
        self.findpath(root, node1, list)
        listone = self.list1
        self.findpath(root, node2, list)
        listtwo = self.list1
        print listone
        print listtwo


    def findpath(self, root, node, list):
        templist = [0]*len(list)
        for i in range(len(list)):
            templist[i] = list[i]
        if root.left:
            if root.left.val == node.val:
                templist.append(0)
                self.list1 = templist
            else:
                templist.append(0)
                self.findpath(root.left, node, templist)
        templist = [0] * len(list)
        for i in range(len(list)):
            templist[i] = list[i]
        if root.right:
            if root.right.val == node.val:
                templist.append(1)
                self.list1 = templist
            else:
                templist.append(1)
                self.findpath(root.right, node, templist)





if __name__ == "__main__":
    s = solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(8)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    s.findcommon(a, f, d)