class Solution(object):
  def addTwoNumbers(self, l1, l2):
  	d1, d2= ListNode(0), ListNode(0)
  	d1.next,d2.next = l1,l2
  	cur1, cur2=d1, d2
  	plus = 0
  	while cur1.next and cur2.next:
  		temp = cur1.next.next
  		new = (cur1.next.val+cur2.next.val+plus)%10
  		plus = (cur1.next.val+cur2.next.val+plus)/10
  		cur1.next = ListNode(new)
  		cur1.next.next = temp
  		cur1,cur2=cur1.next,cur2.next
  	if cur1.next:
  		while cur1.next:
  			temp = cur1.next.next
  			new = (cur1.next.val+plus)%10
  			plus = (cur1.next.val+plus)/10
  			cur1.next = ListNode(new)
  			cur1.next.next = temp
  			cur1 = cur1.next
  		if plus>0: cur1.next,plus = ListNode(plus),0
  	elif cur2.next:
  		while cur2.next:
  			new = (cur2.next.val+plus)%10
  			plus = (cur2.next.val+plus)/10
  			cur1.next = ListNode(new)
  			cur1,cur2 = cur1.next,cur2.next
  		if plus>0: cur1.next,plus= ListNode(plus),0
  	if plus>0: cur1.next = ListNode(plus)
  	return d1.next