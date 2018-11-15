class Solution(object):
    def flatten(self, root):  # use reverse preorder, middle->right->left
        if not root: return root
        root = self.flat(root, None)

    def flat(self, root, pre):
        if not root: return pre # when add the list to a None point
        right = self.flat(root.right, pre)  # add previous list to root.right
        left = self.flat(root.left, right)# add previous list to root.left
        root.right = left#put left list to right
        root.left = None
        return root

# class Solution(object):
#   def flatten(self, root):
#   	if not root:return root
#   	self.construct(root, None)
#
#   def construct(self, root, pre):
#   	if not root: return pre
#   	temp = self.construct(root.right, pre)
#   	root.right= self.construct(root.left, temp)
#   	root.left= None
#   	return root

#    1
#    / \
#   2   5
#  / \   \
# 3   4   6
# -----------
# pre = 5
# cur = 4
#
#     1
#    /
#   2
#  / \
# 3   4
#      \
#       5
#        \
#         6
# -----------
# pre = 4
# cur = 3
#
#     1
#    /
#   2
#  /
# 3
#  \
#   4
#    \
#     5
#      \
#       6
# -----------
# cur = 2
# pre = 3
#
#     1
#    /
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# -----------
# cur = 1
# pre = 2
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6

# not in place method
# class Solution(object): # not in place method
#   def flatten(self, root):
#   	if not root: return root
#   	fromleft = self.flatten(root.left)
#   	root.left = None
#   	pre_right = self.flatten(root.right)
#   	root.right = fromleft
#   	self.addright(root, pre_right)
#   	return root
#   def addright(self, root, pre_right):
#   	if not root.right: root.right = pre_right
#   	else: self.addright(root.right, pre_right)