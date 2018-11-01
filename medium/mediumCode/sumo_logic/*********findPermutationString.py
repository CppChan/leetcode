class Solution(object):
  def checkInclusion(self, a, b):#method 1
  	if len(a)>len(b):return False
  	a_map, b_map, res= [0]*26, [0]*26,[]
  	for i in range(len(a)):
  		a_map[ord(a[i])-ord('a')]+=1
  		b_map[ord(b[i])-ord('a')]+=1
  	count = 0
  	for i in range(len(a_map)):
  		if a_map[i]==b_map[i]:count+=1
  	for i in range(len(b)-len(a)):
  		if count == 26: res.append(i)
  		l,r = ord(b[i])-ord('a'),ord(b[i+len(a)])-ord('a')
  		b_map[r]+=1
  		if b_map[r] == a_map[r]: count+=1
  		elif b_map[r]-1 == a_map[r]:count-=1
  		b_map[l]-=1
  		if b_map[l] == a_map[l]: count+=1
  		elif b_map[l]+1== a_map[l]:count-=1
  	if count == 26: res.append(len(b)-len(a))#here, dont use i!!!!!!
	return res


from collections import Counter
def findAnagrams(self, a, b): # slow method
    if len(a) < len(b): return []
    res, dic, i, j = [], Counter(list(b)), 0, 0
    while j < len(a):
        if a[j] not in dic:dic[a[j]] = -1
        else:dic[a[j]] -= 1
        if dic[a[j]] == 0: dic.__delitem__(a[j])
        if j - i == len(b):
            if a[i] not in dic:dic[a[i]] = 1
            else:dic[a[i]] += 1
            if dic[a[i]] == 0: dic.__delitem__(a[i])
            i += 1
        if len(dic) == 0: res.append(i)
        j += 1
    return res
# from collections import Counter
# class Solution(object):
#   def checkInclusion(self, b, a):
#   	b= list(b)
#   	dic_b = Counter(b)
#   	i, j, need,res,plus,out= 0, 0, len(dic_b),[],0,""
#   	if len(a)<len(b): return False
#   	while i<=j and j<len(a):
#   		if a[j] not in dic_b: dic_b[a[j]],out=-1,a[j]#out is the char that not in b
#   		else:dic_b[a[j]]-=1
#   		if dic_b[a[j]] == 0:need-=1
#   		if dic_b[a[j]]<0:plus+=1
#   		if need == 0 and plus==0: res.append(i)# no need no plus
#   		if plus>0:
#   			while i<=j:
#   				dic_b[a[i]]+=1
#   				if dic_b[a[i]]==1:need+=1#need a letter again
#   				if dic_b[a[i]]==0:plus-=1
#   				i+=1
#   				if plus == 0:break
#   			if out in dic_b: dic_b.__delitem__(out)
#   		j,out=j+1,""
#   	return res

if __name__=="__main__":
    s = Solution()
    print s.checkInclusion("hello","ooohlleooolleh")