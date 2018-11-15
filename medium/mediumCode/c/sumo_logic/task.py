from collections import deque
class Solution(object):
    def sol(self, input):
        input_, out, no_income, res= input.items(), {}, deque([]),[]
        for i in range(len(input_)):
            require = input_[i][1] # [[[0],[]],[[1],[0]]]
            if len(require)==0: no_income.append(int(input_[i][0]))
            for j in require:
                if j not in out: out[j] = [int(input_[i][0])]
                else: out[j].append(int(input_[i][0]))
        print out
        while len(no_income)>0:
            start = no_income.popleft()
            res.append(start)
            if start not in out: continue
            out_point = out[start]
            for e in out_point:
                input[str(e)].remove(start)
                if len(input[str(e)])==0:
                    no_income.append(e)
                    input.__delitem__(str(e))
        return res


from collections import deque
class Solution(object):
    def findOrder(self, n, input):
    	prer, res = [0]*n,[]
    	for i in range(len(input)):
    		prer[input[i][0]]+=1
    	queue = deque([])
    	for i in range(len(prer)):
    		if prer[i]==0:queue.append(i)
    	while len(queue)>0:
    		cur = queue.popleft()
    		res.append(cur)
    		for i in range(len(input)):
    			if input[i][1]==cur:
    				prer[input[i][0]]-=1
    				if prer[input[i][0]]==0: queue.append(input[i][0])
    	if len(res)==n:return res
    	return []

s = Solution()
input = {"0":[], "1":[0,2],"2":[0], "3":[1,2]}
print s.sol(input)