# public class Solution {
#   public void sort(LinkedList<Integer> s1) {
#     Stack<Integer> help=new Stack<Integer>();
#         while(s1.size()>0){
#             int cur=s1.removeFirst();//已将cur弹出，准备压入help
#             while(!help.isEmpty()&&cur>help.peek()){
#                 s1.addFirst(help.pop());
#                 //如果cur大于Help栈顶元素，将help元素逐一弹出、逐一压入stack
#                 //直到cur小于或等于help栈顶元素，再将cur压入help
#             }
#             help.push(cur);//栈顶元素最小，cur≤栈顶，直接压入Help
#         }
#         //到这里为止，stack所有元素都弹出了
#         while(!help.isEmpty()){
#             s1.add(help.pop());//只要help不为空，将排好序的元素逐一弹出、压入到stack
#         }
#   }
# }