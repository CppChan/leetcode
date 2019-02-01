
#Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
# method:
# if num[i]>num[i+1] then num[i] must be remove, also if num[i]<num[i-1], num[i-1]must be remove,
# finally make the array into an ascending array


class Solution(object):
    def removeKdigits(self, num, k):
    	if k>=len(num):return "0"
    	i = 0
    	while i<len(num) and k>0:
    		while i<len(num)-1 and int(num[i])>int(num[i+1]) and k>0:
    			num = num[:i]+num[i+1:]
    			k-=1
    			while i>=1 and int(num[i])<int(num[i-1]) and k>0:
					# here, must be inner while, for example, consider 22210-->2210,
					# now is at 1 after remove a precious 2, then must cosider element before 1, if they are larger than 1
					# but not immediately remove 1
    				num = num[:i-1]+num[i:]
    				i-=1
    				k-=1
    		i+=1
    	while k>0: # dont forget, until now, num is a ascending array, so now begin to remove from back
    		num = num[:-1]
    		k-=1
    	i = 0
    	while len(num)>0 and num[0]=="0":
    		num = num[1:]
    	if len(num)==0:return "0"
    	return num

if __name__=="__main__":
    s = Solution()
    s.removeKdigits("1432219",3)