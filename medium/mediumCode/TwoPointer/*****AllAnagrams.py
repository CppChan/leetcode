class Solution(object):
  def allAnagrams1(self, p,s):
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0]*123, [0]*123
        for x in p:
            phash[ord(x)] += 1
        for x in s[:m-1]:
            shash[ord(x)] += 1 # use ord to indicate ascii
        for i in range(m-1, n):
            shash[ord(s[i])] += 1
            if i-m >= 0:
                shash[ord(s[i-m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res

#https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.

  def allAnagrams(self, p, s):
      if len(s) < len(p): return []
      dic, k, res = {}, len(p), []
      for i in range(len(p)):
          if p[i] not in dic:dic[p[i]] = 1
          else:dic[p[i]] += 1
      i, j = 0, 0
      while j < len(s):
          if len(dic) == 0: res.append(j - k)
          if s[j] in dic:dic[s[j]] -= 1
          elif s[j] not in dic:dic[s[j]] = -1
          if j >= k:
              if s[i] in dic:dic[s[i]] += 1
              elif s[i] not in dic:dic[s[i]] = 1
              if dic[s[i]] == 0: dic.__delitem__(s[i])
              i += 1
          if s[j] in dic and dic[s[j]] == 0: dic.__delitem__(s[j])#if s[j] in dic? because s[i]may =s[j] and maybe deleted previously
          j += 1
      if len(dic) == 0: res.append(j - k)#dont forgot the last loop's operation
      return res


if __name__ == "__main__":
    s = Solution()
    print s.allAnagrams3("aab","ababacbbaac")