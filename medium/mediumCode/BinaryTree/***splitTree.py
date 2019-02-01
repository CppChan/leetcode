class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
# class Solution1(object):
#     def split_tree(self, root, num):
#         res = [None, None]
#         res = self.find(root, num, res, [False, None])
#         if not res[0]:
#             res[0] = root
#         else:
#             res[1] = root
#         return res
#
#     def find(self, root, num, res, hashandle):
#         if root.val == num:
#             return [root.left, root.right]
#         left, right = None, None
#         if root.val > num:
#             left = self.find(root.left, num, res, hashandle)
#         else:
#             right = self.find(root.right, num, res, hashandle)
#         if not hashandle[0]:
#             if left[0] or left[1]:
#                 hashandle[0], hashandle[1] = True, 0
#                 root.left = left[1]
#                 left[1] = None
#                 return left
#             if right[0] or right[1]:
#                 hashandle[0], hashandle[1] = True, 1
#                 root.right = right[0]
#                 right[0] = None
#                 return right
#         if hashandle[1] == 0:
#             return left
#         else:
#             return right

class Solution(object):
	left, right = None, None
	def split_tree(self, root, input):
		if root.val == input:self.left, self.right= root.left, root.right
		else:
			if root.val>input: self.find(root,input, [True])
			else: self.find(root,input, [False])
			if self.left: self.right = root
			else: self.left = root

	def find(self, root, input, goleft):
		if root.val == input:
			if goleft[0]:
				self.left = root.left
				return root.right
			else:
				self.right = root.right
				return root.left
		son = None
		if root.val>input: son = self.find(root.left, input, goleft)
		else:
			goleft[0]=False
			son = self.find(root.right, input, goleft)
		if son:
			if goleft[0]: root.left = son
			else: root.right = son
			return None
		return None


if __name__=="__main__":
    s = Solution()
    a =TreeNode(8)
    b =TreeNode(5)
    c =TreeNode(10)
    d =TreeNode(3)
    e = TreeNode(7)
    f = TreeNode(9)
    g = TreeNode(12)
    a.left, a.right= b,c
    b.left, b.right= d,e
    c.left, c.right =f,g
    e.left = TreeNode(6)
    res = s.split_tree(a,10)
    print res