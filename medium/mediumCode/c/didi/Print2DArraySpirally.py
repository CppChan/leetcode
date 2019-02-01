class Solution(object):
	def prints(self, input):
		i,j,m,n,res= 0, len(input[0])-1, 0, len(input)-1,[]
		while i<j and m<n:
			self.printout(input, i, j, m, n,res)
			i,j,m,n = i+1, j-1, m+1, n-1
		if i==j or m==n:
			if m==n:
				while i<=j:
					res.append(input[m][i])
					i+=1
			elif i==j:
				while m<=n:
					res.append(input[m][i])
					m+=1
		return res
	def printout(self, input, i, j, m, n,res):
		prei,prem= i,m
		while i<j:
			res.append(input[m][i])
			i+=1
		while m<n:
			res.append(input[m][j])
			m+=1
		while i>prei:
			res.append(input[n][i])
			i-=1
		while m>prem:
			res.append(input[m][i])
			m-=1

if __name__=="__main__":
    s =Solution()
    print s.prints([[1,2,3],[5,6,7],[9,10,11],[13,14,15]])