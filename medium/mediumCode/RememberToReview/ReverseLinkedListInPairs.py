# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseInPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while (cur.next and cur.next.next):
            temp1 = cur.next
            cur.next = cur.next.next
            temp1.next = cur.next.next
            cur.next.next = temp1
            cur = cur.next.next
        return dummy.next
