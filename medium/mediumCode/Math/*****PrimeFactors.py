class Solution(object):
  def factors(self, target):
  	i ,res= 2,[]
  	while i*i<=target:#if target has prime factor i whie i*i>target, then target/i must have been add into the res, contradiction
  		while target%i==0:
  			target/=i
  			res.append(i)
  		i+=1
  	if target!=1: res.append(target)#corner
  	return res