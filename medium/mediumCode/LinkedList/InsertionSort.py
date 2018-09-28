class Solution(object):
  def insertionSort(self, head):
  	if not head: return None
  	dummy = ListNode(-10000)
  	dummy.next = head
  	cur, pre, i = dummy.next,dummy, 1
  	while cur.next:
  		if cur.next.val>cur.val:
  			cur=cur.next
  			i+=1
  			continue
  		temp = cur.next.val
  		cur.next = cur.next.next
  		for j in range(i):
  			if pre.val<temp and pre.next and pre.next.val>=temp:
  				back = pre.next
  				pre.next = ListNode(temp)
  				pre.next.next = back
  				break
  			pre = pre.next
  		pre = dummy
  		i+=1
  	return dummy.next