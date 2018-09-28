class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
  def find(self, bst, node1, node2):
  	if node1==node2:return 0
  	isone, istwo = False, False
  	for i in range(len(bst)):
  		if bst[i]==node1:isone = True
  		if bst[i]==node2:istwo = True
  	if not isone or not istwo:return 0
  	bst = sorted(bst)#dont forget
  	root = self.buildTree(bst)
  	if root.val == node1:return self.findNode(root, node2)
  	elif root.val == node2:return self.findNode(root, node1)
  	else:return self.findDis(root, node1, node2)[0]

  def findDis(self, root, node1, node2):
      if not root: return None
      if root.val == node1:
          if self.findNode(root, node2) != None:return (self.findNode(root, node2), True)# dont forget corner case!!
          else:return (1, False)
      if root.val == node2:
          if self.findNode(root, node1) != None:return (self.findNode(root, node1), True)
          else:return (1, False)
      left = self.findDis(root.left, node1, node2)
      right = self.findDis(root.right, node1, node2)
      if not left and not right: return None
      if left and right: return (left[0] + right[0], True)
      if left:
          if left[1]:return left
          else:return (left[0] + 1, False)
      else:
          if right[1]:return right
          else:return (right[0] + 1, False)

  def findNode(self, root, node):
      if not root: return None
      if root.val == node: return 0#here is 0
      left, right = self.findNode(root.left, node), self.findNode(root.right, node)
      if left != None:return left + 1
      elif right != None:return right + 1
      else:return None

  def buildTree(self, bst):
  	if len(bst)==0:return None
  	elif len(bst)==1: return TreeNode(bst[0])
  	mid = (0+len(bst))/2
  	root = TreeNode(bst[mid])
  	root.left = self.buildTree(bst[:mid])
  	root.right = self.buildTree(bst[mid+1:len(bst)])



# def findDist(bstDistance, node1, node2):
#     class TreeNode:
#         def __init__(self, val):
#             self.val = val
#             self.left = None
#             self.right = None
#
#     def findLowestCommonAncestor(root, node1, node2):
#         if node1 > node2: return findLowestCommonAncestor(root, node2, node1)
#         while True:
#             if root.val >= node1 and root.val <= node2: return root
#             if root.val < node1:
#                 root = root.right
#             else:
#                 root = root.left
#
#     def calculateDist(root, node):
#         ret = 0
#         while root.val != node:
#             if node > root.val:
#                 root = root.right
#             else:
#                 root = root.left
#             ret += 1
#         return ret
#
#     if node1 == node2 or not bstDistance: return 0
#     root = TreeNode(bstDistance[0])
#     for i in range(1, len(bstDistance)):
#         node = root
#         while True:
#             if bstDistance[i] > node.val:
#                 if not node.right:
#                     node.right = TreeNode(bstDistance[i])
#                     break
#                 node = node.right
#             else:
#                 if not node.left:
#                     node.left = TreeNode(bstDistance[i])
#                     break
#                 node = node.left
#     node = findLowestCommonAncestor(root, node1, node2)
#     dist1 = calculateDist(node, node1)
#     dist2 = calculateDist(node, node2)
#     return dist1 + dist2
if __name__=="__main__":
    s = Solution()
    bstDistance = [2,0,3,5,6,4,7,8,1]
    node1 = 1
    node2 = 0
    print(s.find(bstDistance, node1, node2))