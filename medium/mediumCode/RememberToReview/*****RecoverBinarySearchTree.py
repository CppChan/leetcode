#in-order search in BST, it should output an array in increasing order

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    preNode = None
    def recover(self, root):
        wrong = []
        self.inOrder(root, wrong)
        temp = wrong[0].val
        wrong[0].val = wrong[1].val
        wrong[1].val = temp
        return root

    def inOrder(self, root, wrong):
        if root.left:
            self.inOrder(root.left, wrong)
        if self.preNode and root.val<=self.preNode.val:
            if len(wrong)==0:
                wrong.append(self.preNode)
                wrong.append(root)
            elif len(wrong)==2:
                wrong[1]=root
        self.preNode = root
        if root.right:
            self.inOrder(root.right, wrong)

if __name__ == "__main__":
    s = Solution()
    a = TreeNode(3)
    b = TreeNode(2)
    c = TreeNode(1)
    a.left = b
    b.right = c
    s.recover(a)