from collections import Counter
class Solution(object):
  def allAnagrams1(self, s,p):
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

  def findAnagrams(self, a, b):
  	if len(a)<len(b):return []
  	res,dic,i,j= [],Counter(list(b)),0,0
  	while j<len(a):
  		if a[j] not in dic: dic[a[j]] = -1
  		else: dic[a[j]]-=1
  		if dic[a[j]]==0:dic.__delitem__(a[j])
  		if j-i==len(b):
  			if a[i] not in dic:dic[a[i]]=1
  			else: dic[a[i]]+=1
  			if dic[a[i]]==0:dic.__delitem__(a[i])
  			i+=1
  		if len(dic)==0:res.append(i)
  		j+=1
  	return res



if __name__ == "__main__":
    s = Solution()
    print s.allAnagrams3("aab","ababacbbaac")