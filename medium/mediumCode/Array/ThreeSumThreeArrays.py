class Solution(object):
  def exist(self, a, b, c, target):
    if len(a)==0 or len(b)==0 or len(c)==0:return False
    list =set([])
    for i in c:
      list.add(target-i)
    for j in list:
        if self.existSum(a,b,j): return True
    return False


  def existSum(self, a, b, target):
    if len(a)==0 or len(b)==0:return False
    list =set([])
    for i in a:
        list.add(target-i)
    for j in b:
        if j in list: return True
    return False