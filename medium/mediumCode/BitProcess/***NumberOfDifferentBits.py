# public class Solution {
#
#     public int diffBits(int a, int b)
#     {
#         return Integer.bitCount(a ^ b);
#     }
# }


class Solution(object):
  def diffBits(self, a, b):
        z = a ^ b#yihuo
        n = 0
        while z > 0:
            n = n + z % 2
            z = z >> 1
        return n