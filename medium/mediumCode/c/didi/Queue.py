class Queue(object):
	def __init__(self):
		self.stack1, self.stack2= [],[]

	def push(self, val):
		self.stack1.append(val)

	def pop(self):
		if len(self.stack2)==0:
			while len(self.stack1)>0:
				self.stack2.append(self.stack1.pop())
		if len(self.stack2)==0:return None
		return self.stack2.pop()


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print q.pop()
print q.pop()
print q.pop()
print q.pop()