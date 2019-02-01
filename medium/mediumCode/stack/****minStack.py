class MinStack: #by myself

    def __init__(self):
        self.stack = []
        self.minstack = []#use to save the min element in each "push" posistion

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.stack)==1: self.minstack.append(x)
        else:
            self.minstack.append(min(x, self.minstack[-1]))
    # @return nothing
    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]


    # @return an integer
    def getMin(self):
        return self.minstack[-1]


class MinStack2:

    min = float('inf')
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if x<=self.min:
            self.q.append(self.min) # save the previous min
            self.min = x
        self.q.append(x)
    # @return nothing
    def pop(self):
        if self.q.pop()==self.min:self.min = self.q.pop() #previous min become min again


    # @return an integer
    def top(self):
        return self.q[-1]


    # @return an integer
    def getMin(self):
        return self.min