from collections import deque
class Stack(object):
	def __init__(self):
		self.main, self.ass = deque([]), deque([])

	def push(self, val):
		self.main.append(val)

	def pop(self):
		if len(self.main) == 0: return None
		while len(self.main)>1:
			self.ass.append(self.main.popleft())
		self.main, self.ass = self.ass, self.main
		return self.ass.popleft()


q = Stack()
q.push(1)
q.push(2)
q.push(3)
print q.pop()
print q.pop()
print q.pop()
print q.pop()