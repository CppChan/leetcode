class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reorderList(self, head):
      if head:
    	dummy = ListNode(0)
    	dummy.next = head
    	cur, cur2= dummy,dummy
    	while cur2 and cur2.next: # a new way to get half
    		cur = cur.next
    		cur2 = cur2.next.next
    	back = cur.next
    	cur.next, stack = None, []
    	while back:
    		stack.append(back)
    		back = back.next
    	cur = dummy.next
    	while cur and len(stack)>0:
    		new= stack.pop()
    		temp = cur.next
    		cur.next = new
    		cur.next.next = temp
    		cur = cur.next.next
# class Solution(object):
#   def reorder(self, head):
#   	dummy = ListNode(0)
#   	dummy.next = head
#   	cur = dummy
#   	size = 0
#   	while cur.next:
#   		size+=1
#   		cur = cur.next
#   	if size == 0 or size == 1: return dummy.next
#   	if size%2 == 0: mid = size/2-1
#   	else: mid = size/2
#   	cur = dummy.next
#   	i = 0
#   	while i<mid:
#   		cur = cur.next
#   		i+=1
#   	midpoint = cur
#   	while cur.next:
#   		cur = cur.next
#   	endpoint = cur
#   	while midpoint.next!=endpoint:
#   		temp1= endpoint.next
#   		temp2 = midpoint.next.next
#   		endpoint.next = midpoint.next
#   		endpoint.next.next = temp1
#   		midpoint.next = temp2
#   	cur = dummy.next
#   	while cur and endpoint:
#   		temp1 = cur.next
#   		cur.next = ListNode(endpoint.val)#pay attenttion, can not write cur.next = endpoint, because will cause dead loop
#   		cur.next.next = temp1
#   		if not endpoint.next and size%2==0:cur = cur.next#corrner case, must use cur.next = None to eliminate useless element, can not cur = None
#   		else:cur = cur.next.next
#   		endpoint = endpoint.next
#   	if cur.next: cur.next = None#corrner case, must use cur.next = None to eliminate useless element, can not cur = None
#   	return dummy.next




if __name__ == "__main__":
    one = ListNode(1)
    one.next = ListNode(2)
    one.next.next = ListNode(3)
    one.next.next.next = ListNode(4)
    s = Solution()
    s.reorder(one)