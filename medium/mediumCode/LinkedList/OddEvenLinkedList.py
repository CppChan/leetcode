# make two dummy pointer odd and even, and then iterate head and add coresponding point to the odd and
# even list, and finally concatecate two lists.

class Solution(object):
  def oddEvenList(self, head):
  	dummy1=odd=ListNode(0)
  	dummy2=even=ListNode(0)
  	i = 0
  	while head:
  		if i%2==0:
  			odd.next=head
  			odd = odd.next
  		else:
  			even.next = head
  			even= even.next
  		head = head.next
  		i+=1
  	even.next = None
  	odd.next = dummy2.next
  	return dummy1.next