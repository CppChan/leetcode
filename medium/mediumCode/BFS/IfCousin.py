from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def isCousin(self, root, a, b):
  	if not root:return False
  	queue = deque([])
  	queue.append(root)
  	size = 1
  	while len(queue)>0:
  		newsize = 0
  		findone = False
  		while size>0:
  			temp = queue.popleft()
  			if temp.left:
  				queue.append(temp.left)
  				newsize+=1
  			if temp.right:
  				queue.append(temp.right)
  				newsize +=1
  			if (temp.left == a and temp.right == b )or (temp.left == b and temp.right ==a):return False
  			elif (temp.left == a or temp.right == b or temp.left == b or temp.right == a)and not findone: findone = True
  			elif (temp.left == a or temp.right == b or temp.left == b or temp.right == a)and findone: return True
  			size-=1
  		size = newsize
  	return False

if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(3)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(5)
    g = TreeNode(0)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    print s.isCousin(a,f,d)