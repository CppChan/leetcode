# easiest solution

# public void rotate(int[] nums, int k) {
#     k %= nums.length;
#     reverse(nums, 0, nums.length - 1);
#     reverse(nums, 0, k - 1);
#     reverse(nums, k, nums.length - 1);
# }
#
# public void reverse(int[] nums, int start, int end) {
#     while (start < end) {
#         int temp = nums[start];
#         nums[start] = nums[end];
#         nums[end] = temp;
#         start++;
#         end--;
#     }
# }



#mysolution:

class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        self.rotate1(nums, k, len(nums), 0)

    def rotate1(self, nums, k, length, start):
        if k == 0 or length == 1: return
        shift, changelen = length - k, min(k, length - k)
        self.exchange(nums, changelen, shift, start)
        if k >= length - k: k -= changelen
        length -= changelen
        start += changelen
        self.rotate1(nums, k, length, start)

    def exchange(self, nums, changelen, shift, start):
        for i in range(changelen):
            nums[start + i], nums[start + i + shift] = nums[start + i + shift], nums[start + i]
