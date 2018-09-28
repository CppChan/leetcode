# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution():
    def mergeSort(self, head):
        i = 0
        dummy = head
        while (head):
            i += 1
            head = head.next
        if (i == 0):
            return None
        result = self.divide(dummy, 0, i - 1)
        return result

    def divide(self, head, start, end):
        if (start == end):
            cur = head
            i = 0
            while (i < start):
                cur = cur.next
                i += 1
            return ListNode(cur.val)
        else:
            mid = (int)(start + end) / 2
            left = self.divide(head, start, mid)
            right = self.divide(head, mid + 1, end)
            mergelist = self.merge(left, right)
            return mergelist

    def merge(self, left, right):
        dummy = ListNode(0)
        cur = dummy#this is important, can not cur = dummy.next
        while (left):
            if (right == None):
                break
            while (right):
                if (left.val < right.val):
                    cur.next = left
                    left = left.next
                    cur = cur.next
                    break
                else:
                    cur.next = right
                    right = right.next
                    cur = cur.next
                    continue
        if (left):
            cur.next = left
        else:
            cur.next = right
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    a =ListNode(2)
    b =ListNode(1)
    a.next = b
    c = s.mergeSort(a)





