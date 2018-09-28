class Solution(object):
    def myAtoi(self, s):
        if len(s) == 0: return 0
        ls = list(s.strip())
        if len(ls)==0:return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-', '+']: del ls[0]#this step is important
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            ret = ret * 10 + int(ls[i])
            i += 1
        return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))#this step is important


if __name__ == "__main__":
    s = Solution()
    print ord('a')-ord('0')