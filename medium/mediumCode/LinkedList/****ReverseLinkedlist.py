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

    #Better solution, do it recursively and iteratively
    def reverseList(self, head):
        if not head: return head
        dummy = ListNode(0)
        cur = head
        while cur.next:
            cur = cur.next
        dummy.next = cur
        self.helper(head, dummy)
        return dummy.next

    def helper(self, point, dummy):
        if not point.next: return point
        back = self.helper(point.next, dummy)
        back.next = point
        point.next = None
        back = back.next
        return back


if __name__ == "__main__":
    one = ListNode(1)
    one.next = ListNode(2)
    one.next.next = ListNode(3)
    s = Solution()
    print s.reverse(one)#should be 3->2->1
