class TreeNode(object):
    def __init__(self,key,val):
        self.left = self.right = None
        self.key = key
        self.val = val

class ImpleBinarySearchTree(object):

    def __init__(self):
        self.__root = None

    def insert(self, key, val):
        self.__root = self.__insert(self.__root, key, val)

    def __insert(self, root, key, val):
        if not root:
            return TreeNode(key, val)
        if root.key<key:
            root.right = self.__insert(root.right, key, val)
        elif root.key>key:
            root.left = self.__insert(root.left, key, val)
        else:
            root.val = val
        return root

    def delete(self, key):
        self.__root = self.__delete(self.__root, key)

    def __delete(self, root, key):
        if root.key<key:
            root.right = self.__delete(root.right, key)
        elif root.key >key:
            root.left = self.__delete(root.left, key)
        if root.key == key:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                new = self.__findMin(root.right)
                new.right= self.__deleteMin(root.right)
                new.left = root.left
                root = new
                return root
        return root

    def __deleteMin(self, root):
        if not root.left and not root.right:
            return None
        elif root.left:
            root.left = self.__deleteMin(root.left)
        elif not root.left:
            return root.right
        return root

    def __findMin(self, root):
        if not root.left:
            return TreeNode(root.key, root.val)
        elif root.left:
            return self.__findMin(root.left)

if __name__ == "__main__":
    s = ImpleBinarySearchTree()
    # a = TreeNode(5,5)
    # b = TreeNode(3,3)
    # c = TreeNode(8,8)
    # d = TreeNode(1,1)
    # e = TreeNode(4,4)
    # f = TreeNode(6,6)
    # g = TreeNode(9,9)
    s.insert(5,5)
    s.insert(3,3)
    s.insert(8,8)
    s.insert(1,1)
    s.insert(4,4)
    s.insert(6,6)
    s.insert(9,9)
    s.delete(3)
    s.delete(6)
    s.delete(9)
