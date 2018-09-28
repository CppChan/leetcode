import random
class Solution(object):
    def __init__(self):
        self.res = []

    def read(self, value):
        self.res.append(value)

    def sample(self):
    	if len(self.res)==0:return None
    	index = int(random.randint(0,len(self.res)-1))
    	return self.res[index]