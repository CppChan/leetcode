class Solution(object):
	def Longest_contained_range(self, array):
		dic = set(array)
		res = 0
		max = 1
		i = 0
		while(dic and i<len(array) and len(dic)>res):
			if(array[i] in dic):
				dic.remove(array[i])
				left = array[i]-1
				right = array[i]+1
				while(left in dic):
					dic.remove(left)
					max+=1
					left-=1
				while(right in dic):
					dic.remove(right)
					max+=1
					right+=1
			if max>res:
				res = max
			max = 1
			i+=1






if __name__ == "__main__":
    s = Solution()
    s.Longest_contained_range([-1,3,2,5,9,11,4])
            #         right+=1
            # if max>res:
            #     res = max
            #     max = 1
            #     i+=1
            # return res

