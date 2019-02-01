class Solution(object):
	def findmax(self, input):
		mint,maxt = min(input), max(input)
		time = [0]*(maxt-mint+1)
		for i in range(len(input)-1):
			start, end = min(input[i],input[i+1]),max(input[i],input[i+1])
			time[start-mint]+=1 # like open a new room
			time[end-mint]-=1 # close a room
		res,num = 0,0
		for j in range(len(time)):
			num+=time[j]
			res = max(res, num) # when room are open the most
		return res

s=Solution()
print s.findmax([2,5,1,6,9])