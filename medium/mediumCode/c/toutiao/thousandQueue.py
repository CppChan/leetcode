from collections import deque
class Queue(object):
	def __init__(self, q_len, subq_len):
		self.q_len, self.subq_len = subq_len
		self.queue, self.full= deque([]), False

	def add(self, num):
		if self.full:return
		self.queue[-1].append(num)
		if len(self.queue[-1])==self.subq_len:
			if len(self.queue)==self.q_len: self.full = True
			else:
				self.queue.append(deque([]))

	def pop(self):
		return self.queue[0].popleft()
		if len(self.queue[0])==0:
			self.queue.popleft()
			if self.full:self.full=False