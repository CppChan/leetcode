from collections import deque


class Codec:

    def serialize(self, root):
        if not root: return None
        queue, res = deque([root]), str(root.val)
        while len(queue) > 0:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                res += "." + str(node.left.val) #Remember to use "." as split in case that the node val is 34,12,....
            else:
                res += ".*"
            if node.right:
                queue.append(node.right)
                res += "." + str(node.right.val)
            else:
                res += ".*"
        return res

    def deserialize(self, data):
        if not data: return None
        data = data.split(".")
        root = TreeNode(int(data[0]))
        queue, i = deque([root]), 1
        while i < len(data):
            node = queue.popleft()
            if data[i] == "*":
                node.left = None
            else:
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            if i + 1 >= len(data): break
            if data[i + 1] == "*":
                node.right = None
            else:
                node.right = TreeNode(int(data[i + 1]))
                queue.append(node.right)
            i += 2
        return root
