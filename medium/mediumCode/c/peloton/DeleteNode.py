class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
  def deleteNode(self, length, Node, val):
  	dummy = ListNode(0)
  	dummy.next = Node
  	current = dummy
  	while current.next:
  		if current.next.val>val:
  			current.next = current.next.next
  			continue
  		current = current.next
  	return dummy.next

if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(5)
    e = ListNode(16)
    f = ListNode(3)
    a.next =b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    print s.deleteNode(6, a, 4)
    z = 1