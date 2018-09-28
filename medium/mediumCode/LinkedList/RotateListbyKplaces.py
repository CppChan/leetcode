class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
  def rotateKplace(self, head, n):
  	dummy = ListNode(0)
  	dummy.next = head
  	cur = dummy
  	size = 0
  	while cur.next:
  		size+=1
  		cur = cur.next
  	if size == 0 or size == 1 or n == 0: return dummy.next
  	while n>size:
  		n-=size
  	if n == size: return dummy.next
  	pre = size - n
  	cur = dummy
  	i = 0
  	while i < pre:
  		cur = cur.next
  		i+=1
  	post = cur.next
  	cur.next = None
  	newpre = dummy.next
  	cur = post
  	while cur.next:
  		cur = cur.next
  	cur.next = newpost
  	return post