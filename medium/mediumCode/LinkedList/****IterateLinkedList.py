class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
  def reverse(self, head):
  	dummy = ListNode(0)
  	dummy.next = head
  	front, back, num = dummy, dummy,0
  	while back.next:
  		back = back.next
  		num+=1
  	while num>1 and back:
  		back.next = ListNode(front.next.val)#cannot back.next = front.next, because it also cause cycle in linkedlist
  		back = back.next
  		front.next = front.next.next
  		num-=1
  	return dummy.next

if __name__ == "__main__":
    one = ListNode(1)
    one.next = ListNode(2)
    one.next.next = ListNode(3)
    s = Solution()
    print s.reverse(one)#should be 1->2->3