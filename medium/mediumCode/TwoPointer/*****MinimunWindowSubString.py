import collections
class Solution(object):
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):#index begin at 1
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:#not missing=> missing = 0
                while i < j and need[s[i]] < 0:#if need[c]<0, means now total num of c is higher than what t need, so here left narrow the window
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    def minWindow2(self, s, t):# ignore
        t = list(t)
        dic, letter, i, j, res, ret = {}, set(t), 0, 0, float('inf'), ""
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]] = 1
            else:
                dic[t[i]] += 1
        i = 0
        while i < len(s) and j < len(s):
            while j < len(s):
                if len(letter) == 0 and j - i + 1 < res: res, ret = j - i + 1, s[i:j + 1]
                if s[j] in dic:
                    dic[s[j]] -= 1
                    if dic[s[j]] <= 0 and s[j] in letter: letter.remove(s[j])
                if len(letter) == 0 and s[j] in dic and dic[s[j]] < 0 and s[j] == s[i]: break
                j += 1
            if j<len(s) and len(letter) == 0 and s[j] in dic and dic[s[j]] < 0 and s[j] == s[i]:
                while i < j:
                    if s[i] in dic:
                        if dic[s[i]] < 0:
                            dic[s[i]] += 1
                        else:
                            break
                    i += 1
                if j - i + 1 < res: res, ret = j - i + 1, s[i:j + 1]
        return ret

    def minWindow3(self, s, p):# by myself
        if len(s) < len(p) or len(p) == 0: return ""
        dic, res, ret = {}, float('inf'), ""
        for i in range(len(p)):
            if p[i] not in dic:dic[p[i]] = 1
            else:dic[p[i]] += 1
        i, j, count = 0, 0, len(dic)
        while j < len(s):
            while j < len(s) and count > 0:
                if s[j] in dic:
                    dic[s[j]] -= 1
                    if dic[s[j]] == 0: count -= 1
                j += 1
            while i < j and count == 0:
                if s[i] in dic:
                    dic[s[i]] += 1
                    if dic[s[i]] > 0:
                        count += 1
                i += 1
            if j - i+1 < res: res, ret = j - i, s[i-1:j]
        return ret


if __name__ == "__main__":
        s = Solution()
        print s.minWindow3("AEFBGFCMNDCUIBA","ABCD")

        # a = 4
        # a-= 3>0
        # b = 1
        # print not b
        # print a