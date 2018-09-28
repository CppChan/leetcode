class Solution(object):
  def reverseAlternate(self, head):
  	d,temp = ListNode(0),None
  	d.next= head
  	cur = d.next
  	while cur:
  		if cur.next:
  			newhead = ListNode(cur.next.val)
  			newhead.next= temp
  			temp = newhead
  			cur.next=cur.next.next
  		cur = cur.next #must write this out of if, ow dead recursion
  	cur = d
  	while cur.next:
  		cur = cur.next
  	cur.next = temp
  	return d.next