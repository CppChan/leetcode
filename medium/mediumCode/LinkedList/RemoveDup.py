class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
  def removeDup(self, head):
  	dummy = ListNode(0)
  	dummy.next = head
  	cur = dummy
  	dup = False
  	while cur.next and cur.next.next:
  		if cur.next.val == cur.next.next.val
  			cur.next = cur.next.next
  			dup = True
  			continue
  		if dup:
  			cur.next=cur.next.next
  			dup = False
  			continue
  		cur = cur.next
  	if dup: cur.next = cur.next.next
  	return dummy.next