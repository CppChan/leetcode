# public class Solution {
#   int index = 0;
#   public int[] postOrder(int[] pre, int[] in) {
#     ArrayList<Integer>res = new ArrayList<Integer>();
#     if(in.length==0)return new int[]{};
#  		findpost(res, pre, in);
#     int[]r = new int[res.size()];
#     for(int i = 0 ;i<res.size();i++){
#     	r[i]=res.get(i);
#     }
#     return r;
#   }
#   public void findpost(ArrayList<Integer>res, int[] pre, int[] in){
#   	int center = pre[index];
#     if(in.length==1 && in[0]==center){
#     	res.add(center);
#       return;
#     }
#   	for( int i =0;i<in.length; i++){
#     	if (in[i] ==center){
#         if (i>0){
#           int[]left = Arrays.copyOfRange(in, 0, i);
#           index++;
#           findpost(res, pre, left);
#         }
#         if (i<in.length-1){
#           int[]right = Arrays.copyOfRange(in, i+1, in.length);
#           index++;
#           findpost(res, pre, right);
#         }
#         res.add(center);
#       }
#     }
#   }
# }