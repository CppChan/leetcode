class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        dummy.next = l1;
        cur = dummy
        while cur.next and l2:
            while cur.next and l2 and cur.next.val<=l2.val:
                cur = cur.next
            temp = cur.next
            cur.next = l2
            l2 = l2.next
            cur.next.next = temp
            cur = cur.next
        if l2: cur.next = l2
        return dummy.next