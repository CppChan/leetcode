class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
  def reconstruct(self, level):
  	if len(level)==0:return None
  	root = TreeNode(level[0])
  	level.pop(0)
  	list = deque([(root, -float('inf'), float('inf'))])
  	while len(list)>0 and len(level)>0:
  		temp = list.popleft()
  		if len(level)>0 and level[0]<temp[0].val and level[0]>temp[1]:
  			temp[0].left = TreeNode(level[0])
  			list.append((temp[0].left, temp[1], temp[0].val))
  			level.pop(0)
  		if len(level)>0 and level[0]>temp[0].val and level[0]<temp[2]:
  			temp[0].right = TreeNode(level[0])
  			list.append((temp[0].right,temp[0].val, temp[2]))
  			level.pop(0)
  	return root

if __name__ == "__main__":
    s = Solution()
    s.reconstruct([5,3,10,4,8,9])