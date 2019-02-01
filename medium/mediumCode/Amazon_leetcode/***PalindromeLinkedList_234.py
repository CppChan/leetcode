class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next: return True
        dummy = ListNode(0)
        dummy.next = head
        cur1, cur2 = dummy.next, dummy.next
        while cur2 and cur2.next:
            cur2 = cur2.next.next
            cur1 = cur1.next
        if cur2: cur1 = cur1.next
        cur1 = self.reverse(cur1)
        cur2 = dummy.next
        while cur1:
            if cur1.val != cur2.val: return False
            cur1, cur2 = cur1.next, cur2.next
        return True

    def reverse(self, point):
        nexthead = point.next
        point.next = None
        while nexthead:
            temp = nexthead.next
            nexthead.next = point
            point = nexthead
            nexthead = temp
        return point

# FROM the middle point, reverse the second part of the linkedlist

