class Solution(object):
  def isPalindrome(self, head):
  	d = ListNode(0)
  	d.next = head
  	cur = d
  	size = 0
  	while cur.next:
  		size+=1
  		cur = cur.next
  	cur = d.next
  	i,j,temp1,k= 1, size, None,1
  	while i<j:
  		temp1 = cur
  		while k<j:
  			cur = cur.next
  			k+=1
  		if temp1.val!=cur.val: return False
  		j-=1
  		i+=1
  		k=i
  		cur = temp1.next
  	return True