class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
  def find(self, root):
  	if not root:return 0
  	left,right, res= (0,0),(0,0),[0]
  	if root.left:left = self.avg(root.left,res)
  	if root.right: right = self.avg(root.right,res)
  	return max(res[0],float((left[0]*left[1]+right[0]*right[1]+root.val))/float((left[1]+right[1]+1)))

  def avg(self, root,res):
  	if not root.left and not root.right: return(root.val, 1)
  	left,right = (0,0),(0,0)
  	if root.left: left = self.avg(root.left,res)
  	if root.right: right = self.avg(root.right,res)
  	tempavg = float((left[0]*left[1]+right[0]*right[1]+root.val))/float((left[1]+right[1]+1))
  	res[0]=max(res[0], tempavg)
  	return (tempavg, left[1]+right[1]+1)

if __name__=="__main__":
    root = TreeNode(3)
    root.left, root.right= TreeNode(5), TreeNode(6)
    root.left.left,root.left.right = TreeNode(2), TreeNode(4)
    root.right.left, root.right.right = TreeNode(7), TreeNode(2)
    s = Solution()
    print s.find(root)