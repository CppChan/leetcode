class Solution(object):
  def largestSum(self, array):
    res = -float('inf')
    if len(array)==0:
      return 0
    pre = [0]*len(array)
    pre[0]=array[0]
    for i in range(1,len(array)):
      if pre[i-1]<=0:
        pre[i]=array[i]
      else:
        pre[i]=pre[i-1]+array[i]
    for j in pre:
      res = max(res, j)
    return res

#Lagest Subarray Product:

# public class Solution {
#   public double largestProduct(double[] array) {
#     double[]dp1 = new double[array.length];
#     double[]dp2 = new double[array.length];
#     for(int i = 0; i<array.length; i++){
#       if(i ==0){
#       	dp1[i]= array[i];
#         dp2[i]=	array[i];
#       }else{
#         if (array[i]>=0){
#           dp1[i] = Math.max(dp1[i-1]*array[i], array[i]);
#           dp2[i] = dp2[i-1]*array[i];
#         }else if(array[i]<0){
#         	dp1[i] = dp2[i-1]*array[i];
#           dp2[i] = Math.min(dp1[i-1]*array[i], array[i]);
#         }
#       }
#     }
#     double res = -1000000000.0;
#     for(int j = 0; j<array.length; j++){
#     	res = Math.max(res, dp1[j]);
#     }
#     return res;
#   }
# }