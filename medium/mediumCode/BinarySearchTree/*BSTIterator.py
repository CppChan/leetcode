class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        if root: self.stack.append(root)
        self.addleft(root)

    def hasNext(self):
        if len(self.stack) > 0: return True

    def next(self):
        if len(self.stack) == 0: return None
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
            self.addleft(node.right)
        return node.val

    def addleft(self, root):
        while root and root.left:
            self.stack.append(root.left)
            root = root.left


