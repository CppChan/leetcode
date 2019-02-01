class Solution(object):
    def getIntersectionNode(self, headA, headB):
        la, lb = self.getlen(headA), self.getlen(headB)
        if lb < la: headB, headA = headA, headB
        dif = abs(lb - la)
        while dif > 0:
            headB = headB.next
            dif -= 1
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    def getlen(self, point):
        length = 0
        while point:
            point = point.next
            length += 1
        return length