class Solution(object):
  def nthSuperUglyNumber(self, n, primes):
  	ugly,idx= [0]*n, [0]*len(primes)
  	ugly[0]=1
  	for i in range(1, n):
  		ugly[i]=float('inf')
  		for j in range(len(primes)):
  			if primes[j] * ugly[idx[j]]==ugly[i-1]:idx[j]+=1
  			ugly[i]=min(ugly[i],primes[j] * ugly[idx[j]])
  	return ugly[n-1]


#idx for primes is the num in ugly that primes[i] need to multiply in next round

#each time, ugly[i]'s result is every prime multiply its corresponding element in ugly(which is the minimum)

if __name__=="__main__":
    s = Solution()
    print s.nthSuperUglyNumber(110,[2,3,5,7])