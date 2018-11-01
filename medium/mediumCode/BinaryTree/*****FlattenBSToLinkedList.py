class Solution(object):
  def flatten(self, root):# use reverse preorder, middle->right->left
  	if not root: return root
  	root = self.flat(root,None)
  def flat(self, root, pre):
  	if not root: return pre
  	right = self.flat(root.right, pre)#add previous list to root.right
  	left = self.flat(root.left, right)
  	root.right = left
  	root.left = None
  	return root

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