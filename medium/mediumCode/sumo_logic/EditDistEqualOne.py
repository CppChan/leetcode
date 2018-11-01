import heapq
class Solution(object):
	def findsimilar(self, target, word):
		res = []
		for i in range(len(word)):
			if self.editdist(word[i], target): res.append(word[i])
		return res
	def editdist(self, one, two):
		diff=0
		if len(one)==len(two):
			for i in range(len(one)):
				if one[i]!=two[i]:diff+=1
				if diff>1:return False
			return True
		elif abs(len(one)-len(two))==1:
			if len(one)>len(two):two,one = one, two
			i,j,diff= 0,0,0
			while i <len(one) and j <len(two):
				if one[i]!=two[j]:
					diff+=1
					if diff>1:return False
					j+=1
					continue
				i+=1
				j+=1
			return True
		else:return False

if __name__=="__main__":
    s = Solution()
    print s.findsimilar('apple',['appde','applq', 'bpple', 'applee', 'appl', 'apople', 'acele','','dapple'])