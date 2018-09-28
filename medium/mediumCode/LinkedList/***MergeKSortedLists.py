# public class Solution {
# 	public ListNode merge(List<ListNode> listOfLists) {
# 		PriorityQueue<ListNode>queue = new PriorityQueue<ListNode>(new Comparator<ListNode>() {
# 			@Override
# 			public int compare(ListNode o1, ListNode o2) {
# 				return o1.value-o2.value;
# 			}
# 		});
# 		ListNode dummy = new ListNode(0);
# 		ListNode cur = dummy; #!!!!!!!!!!!!!!!!!!cannot cur = dummy.next , then cur is null, donot belong to dummy, explain as below
#     if (listOfLists.size()==0)return dummy.next;
# 		for (int i = 0; i<listOfLists.size(); i++) {
#       if(listOfLists.get(i)!=null)queue.add(listOfLists.get(i));
# 		}
# 		while(queue.size()>0) {
# 			ListNode temp = queue.remove();
# 			cur.next= temp;#!!!!!!!!!!!!!!!!!!cannot cur = temp
# 			cur = cur.next;
# 			if(temp.next!=null) {
# 				queue.add(temp.next);
# 			}
# 		}
# 		return dummy.next;
# 	}
# }
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
if __name__ == "__main__":
    one = ListNode(1)
    one.next = ListNode(2)
    one.next.next = ListNode(3)
    one.next.next.next = ListNode(4)
    two = one.next
    two = ListNode(5)#wont change one.next
    two.next = ListNode(6)#wont change one.next.next
    # two.next = ListNode(5)
    print one.next.val
    print one.next.next.val
