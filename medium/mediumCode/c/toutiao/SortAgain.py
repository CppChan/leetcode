# 一个数组，每个位置的值对应下标。重新排列，要求对应位置上不能有同下标相同的值，即原先a[0]=0，重排后a[0]不可以等于0。输出总共有多少种重新排列的方法。*

class Solution(object):
	# def find(self, length):
	# 	if length == 0 or length == 1: return 0
	# 	elif length == 2: return 1
	# 	res = length-1
	# 	for i in range(2, length/2):
	# 		res += (self.find(i)+self.find(length-i))* self.C(length, i)

# for example, 0,1,2,3,4,5 can be consider two case
# every element maintain the sort but just move one position, like 1,2,3,4,5,0 => res+4
# set subgroup, like C(2,6), C(3,6), for the subgroup, use the upper rule
	def C(self, length, i):
		down, up= 1,1
		for i in range(1, i+1):
			down*=i
		for i in range(length-i+1, length+1):
			up = up*i
		return up/down

	def find(self, length):
		if length<2:return 0
		if length == 2: return 1
		dp = [0]*(length+1)
		dp[2]=1
		for i in range(3,length+1):
			dp[i]=i-1
			for j in range(2, i/2+1):
			    if j == i/2 and i%2==0: dp[i]+=self.C(i, j)/2*(dp[j]*dp[i-j])
			    else: dp[i]+=(dp[j]*dp[i-j])*self.C(i, j)
		return dp[length]

if __name__=="__main__":
    s = Solution()
    print s.find(5)
    print s.C(5,2)
