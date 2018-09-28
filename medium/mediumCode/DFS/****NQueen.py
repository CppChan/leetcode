import copy
class Solution(object):
    def nqueens(self, n):
    	if n == 1: return[[0]]
    	if n == 2 or n ==3: return []
    	res,state= [],[]
    	self.find(n, res, state)
    	return res

    def find(self, n, res, state):
        if len(state)==n:
            res.append(state[:])
            return
        for i in range(n):
            if self.isValid(state, i):
                state.append(i)
                self.find(n, res, state)
                state.pop()

    def isValid(self, state, i):
        for j in range(len(state)):
            if abs(state[j]-i) == len(state)-j: return False
            #here, maintain state[j]-j!=i-len(state) && state[j]+j!=len(state)+i
            if state[j]==i:return False
        return True

if __name__ == "__main__":
    s =Solution()
    print s.nqueens(5)