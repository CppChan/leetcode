class Solution(object):
    def validParenthesis(self, num):
        res = []
        self.helper(res, '', num, 0, 0)
        print res

    def helper(self, res, pre, num, left, right):
        if left == num:
            res.append(pre+ ')'*(num-right))
        elif left<num:
            if left>right:
                self.helper(res, pre+'(', num, left+1, right)
                self.helper(res, pre+')', num, left, right+1)
            elif left == right:
                self.helper(res, pre+'(', num, left+1, right)

if __name__=='__main__':
    s= Solution()
    s.validParenthesis(3)
