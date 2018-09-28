#Solution1:Fast speed will always catches up with low speed

# public boolean hasCycle(ListNode head) {
#     if (head == null || head.next == null) {
#         return false;
#     }
#     ListNode slow = head;
#     ListNode fast = head.next;
#     while (slow != fast) {
#         if (fast == null || fast.next == null) {
#             return false;
#         }
#         slow = slow.next;
#         fast = fast.next.next;
#     }
#     return true;
# }

class Solution2(object):
  def checkCycle(self, head):
  	dic = set([])
  	while head:
  		if head not in dic: dic.add(head)
  		else:return True
  		head = head.next
  	return False