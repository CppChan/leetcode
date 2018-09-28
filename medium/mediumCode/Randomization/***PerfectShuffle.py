# public class Solution {
#   Random rand = new Random();
#   public void shuffle(int[] array) {
#     for (int i = 0; i < array.length; i++) {
#       swapAt(array, i, randRange(i, array.length));
#     }
#   }
#     private int randRange(int min, int max) {
#         return rand.nextInt(max - min) + min;
#     }
#     private void swapAt(int[] array, int i, int j) {
#         int temp = array[i];
#         array[i] = array[j];
#         array[j] = temp;
#     }
# }