class Solution(object):
  def canJump(self, array):
  	if len(array)==1:return True
  	dp, nearest= [False]*len(array), len(array)-1
  	for i in range(len(array)-1,-1,-1):
  		if i == len(array)-1:dp[i]=True
  		else:
  			if nearest-i<=array[i]:
  				dp[i]=True
  				nearest = i
  	return dp[0]

class Solution2(object):#Determine the minimum number of jumps you need to jump to the end.
  def minJump(self, array):
  	if len(array)==1:return 0
  	dp, nearest= [-1]*len(array), len(array)-1
  	for i in range(len(array)-1,-1,-1):
  		if i == len(array)-1:dp[i]=0
  		else:
  			if nearest-i<=array[i]:
  				nearest = i#dont forget
  				temp = float('inf')
  				for j in range(nearest, i+array[i]+1):
  					if j<len(array) and dp[j]>-1:temp = min(temp,dp[j])
  				dp[i]=temp+1
  			else: dp[i]=-1
  	return dp[0]

class Solution3(object):#Determine the minimum number of jumps you need to jump out of the array.
  def minJump(self, array):
  	dp, nearest= [-1]*len(array), len(array)
  	for i in range(len(array)-1,-1,-1):
  		if i == len(array)-1:
  			if array[i]>0:
  				dp[i]=1
  				nearest = i
  		else:
  			if nearest-i<=array[i]:
  				nearest = i
  				if nearest == len(array) or i+array[i]>=len(array):
  					dp[i]=1
  					continue
  				temp = float('inf')
  				for j in range(nearest, i+array[i]+1):
  					if j<len(array) and dp[j]>-1:temp = min(temp,dp[j])
  				dp[i]=temp+1
  			else: dp[i]=-1
  	return dp[0]