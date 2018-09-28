class Solution(object):
  def merge(self, one, two):
  	if not one:return two
  	if not two:return one
  	main, plus = None, None
  	if one.val>=two.val:main,plus= two,one
  	else:main,plus = one,two
  	dummy,temp= ListNode(0),None
  	dummy.next,cur = main, dummy
  	while cur.next and plus:
  		if plus.val<cur.next.val:
  			temp = cur.next
  			cur.next = ListNode(plus.val)
  			cur.next.next = temp
  			cur,plus= cur.next,plus.next
  		else:cur = cur.next
  	if plus: cur.next = plus#corner case, remember to add the remain list
  	return dummy.next