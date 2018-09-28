class Solution(object):
  def canMerge(self, a, b, c):
    i,j,k=0,0,0
    if len(a)+len(b)!=len(c): return False
    return self.dfs(a,b,c,i,j,k)

  def dfs(self, a,b,c,i,j,k):
    if k==len(c) and i ==len(a) and j==len(b):return True
    if i<len(a) and a[i]==c[k] and self.dfs(a,b,c,i+1,j,k+1):return True
    if j<len(b) and b[j]==c[k] and self.dfs(a,b,c,i,j+1,k+1):return True
    return False