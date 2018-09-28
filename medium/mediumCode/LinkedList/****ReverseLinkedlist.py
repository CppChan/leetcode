class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def reverse(self, head):
  	dummy = ListNode(0)
  	dummy.next = head
  	front, num = dummy.next, 0
  	while front and front.next:
  		temp = dummy.next
  		dummy.next = ListNode(front.next.val)#cannot dummy.next = front next, because then it will become a cycle in linkedlist
  		dummy.next.next = temp
  		front.next = front.next.next
  	return dummy.next

if __name__ == "__main__":
    one = ListNode(1)
    one.next = ListNode(2)
    one.next.next = ListNode(3)
    s = Solution()
    print s.reverse(one)#should be 3->2->1
