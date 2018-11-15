from collections import defaultdict
class Solution(object):
    def maxPoints(self, points):
        if len(points)==1:return 1 #corner case if only one point
    	dic, k_d,has_add,res = defaultdict(lambda:0), defaultdict(lambda:0), {}, 0
    	for point in points:
    		t = (float(point[0]),float(point[1]))
    		dic[t]+=1
    	dic_item = dic.items()
        if len(dic)==1:return dic_item[0][1] #corner case !!!  if (1,1),(1,1)...
    	for i in range(len(dic_item)):
    		for j in range(i+1, len(dic_item)):
    			param= self.compute(dic_item[i][0], dic_item[j][0])
    			if param not in has_add: has_add[param]=set([])
    			if dic_item[i][0] not in has_add[param]:
    				k_d[param]+=dic_item[i][1]
    				has_add[param].add(dic_item[i][0])
    			if dic_item[j][0] not in has_add[param]:
    				k_d[param]+=dic_item[j][1]
    				has_add[param].add(dic_item[j][0])
    			res = max(res, k_d[param])
    	return res
    def compute(self, p1, p2):
    	y_dif,x_dif = p2[1]-p1[1],p2[0]-p1[0]
    	if x_dif ==0: return (p1[0])
    	k = y_dif/x_dif
    	d = p1[1]-k*p1[0]
    	return (k, d)

if __name__=="__main__":
    s = Solution()
    print s.maxPoints([[0,0],[94911151,94911150],[94911152,94911151]])