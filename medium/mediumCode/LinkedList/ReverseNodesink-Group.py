class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
  def reverseKGroup(self, head, k):
  	dummy = ListNode(0)
  	dummy.next = head
  	cur = dummy
  	size=0
  	while cur.next:
  		cur = cur.next
  		size+=1
  	cur = dummy
  	if k>size or k == 1:return dummy.next
  	iter = size/k
  	temp1 = temp2 = end = None
  	for i in range(iter):
  		end = cur
  		for j in range(k):
  			end = end.next
  		for j in range(k-1):
  			temp2 = end.next
  			temp1 = cur.next
  			cur.next = cur.next.next
  			end.next = temp1
  			end.next.next = temp2
  		for j in range(k):
  			cur = cur.next
  	return dummy.next