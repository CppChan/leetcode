class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def reconstruct(self, inOrder, preOrder):
  	if len(inOrder)==0: return None
  	return self.construct(inOrder, preOrder)

  def construct(self, inOrder, preOrder):
  	if len(preOrder)>0:
  		root = TreeNode(preOrder[0])
  		place = inOrder.index(preOrder[0])
  		preOrder.pop(0)# preOrder = preOrder[1,len(preOrder)] wont work, because this will refer preOrder to a new Object
  		if place > 0 and len(inOrder)>1:
  			newinOrder = inOrder[0:place]
  			root.left = self.construct(newinOrder,preOrder)
  		if place<len(inOrder)-1 and len(inOrder)>1:
  			newinOrder = inOrder[place+1:len(inOrder)]
  			root.right = self.construct(newinOrder,preOrder)
  		return root

  def reconstruct2(self, inOrder, postOrder):
  	if len(inOrder)==0: return None
  	return self.construct2(inOrder, postOrder)

  def construct2(self, inOrder, postOrder):
  	if len(postOrder)>0:
  		root = TreeNode(postOrder[-1])
  		place = inOrder.index(postOrder[-1])
  		postOrder.pop(-1)
    	if place<len(inOrder)-1 and len(inOrder)>1:
  			root.right = self.construct2(inOrder[place+1:len(inOrder)],postOrder)
        if place > 0 and len(inOrder)>1:
  			root.left = self.construct2(inOrder[0:place],postOrder)
        return root

  def reconstruct3(self, inOrder, levelOrder):
  	if len(inOrder)==0: return None
  	return self.construct3(inOrder, levelOrder)

  def construct3(self, inOrder, levelOrder):
  	if len(levelOrder)>0:
  		for i in range(len(levelOrder)):
  			if levelOrder[i] in inOrder:break
  		root = TreeNode(levelOrder[i])
  		place = inOrder.index(levelOrder[i])
  		levelOrder.pop(i)
  		if place > 0 and len(inOrder)>1:
  			root.left = self.construct3(inOrder[0:place],levelOrder)
  		if place<len(inOrder)-1 and len(inOrder)>1:
  			root.right = self.construct3(inOrder[place+1:len(inOrder)],levelOrder)
  		return root

if __name__ =="__main__":
    # list = [1,2,3]
    # list = list[1:len(list)]
    # print list
    s = Solution()
    root = s.reconstruct2([1, 3, 4, 5, 8, 11],[1, 4, 3, 11, 8, 5])
    a = 1