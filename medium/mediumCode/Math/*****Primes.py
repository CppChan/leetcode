class Solution(object):
  def primes(self, target):
  	if target<2:return []
  	prime = []
  	notPrime = [False]*(target+1)
  	notPrime[0],notPrime[1]=True,True
  	for i in range(2,target+1):
  		if not notPrime[i]:prime.append(i)
  		for j in range(len(prime)):
  			if prime[j]*i>target:break#remember to judge this
  			notPrime[prime[j]*i]=True
  			if i%prime[j]==0:break
  	return prime

#https://blog.csdn.net/nk_test/article/details/46242401

#Generally, each heshu is multiplied by primes, so make i*prime[j](previous primes) to be notPrime(also, heshu*heshu canbe represented by prime*heshu),
#so not add i*j(for j<i)

#for example, when iterate i == 16, 16%2==0 then break, because 16*3=48 will be covered by 24*2 when iterate 24(since 16 contains factor 2), so break