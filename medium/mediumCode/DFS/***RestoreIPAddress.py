class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, res, [], len(s), 0)
        return res
    def dfs(self, s, res, temp, length, i):
        if len(temp)==4:
            if int(temp[-1])<256:
                if temp[-1][0]=="0" and len(temp[-1])>1:return # for last occation like ".010", should not count into result
                res.append(".".join(temp))
            return
        for k in range(0,3):
            if i+k<len(s) and int(s[i:i+k+1])<256 and length-1-i-k>=(3-len(temp)) and length-1-i-k<=3*(3-len(temp)):# maintain future length meet the need
                temp.append(s[i:i+k+1])
                self.dfs(s, res, temp, length, i+k+1)
                temp.pop(-1)
                if s[i]=="0":break#if s[i]=="0", we just need to consider the "0." occation, not for like "010" occation