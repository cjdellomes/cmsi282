class PriorityQueue:

	def __init__(self):
		self.heap = []

	def add(self, x):
		self.heap.append(x)
		self.sift_up(len(self.heap) - 1)
		return self

	def peek(self):
		return self.heap[0]

	def remove(self):
		if len(self.heap) == 0:
			raise Exception()
		elif len(self.heap) == 1:
			self.heap = []
		else:
			self.heap[0] = self.heap.pop()
			self.sift_down(0)

	def sift_up(self, item):
		parent = int((item - 1) / 2)
		truth = self.heap[parent] > self.heap[item]
		if parent >= 0 and truth:
			temp = self.heap[parent]
			self.heap[parent] = self.heap[item]
			self.heap[item] = temp
			self.sift_up(parent)

	def sift_down(self, item):
		child = (item * 2) + 1
		if child >= len(self.heap):
			return self
		if child + 1 < len(self.heap) and self.heap[child] > self.heap[child+1]:
			child += 1
		if self.heap[item] > self.heap[child]:
			temp = self.heap[child]
			self.heap[child] = self.heap[item]
			self.heap[item] = temp
			self.sift_down(child)

	def __len__(self):
		return len(self.heap)

	def __str__(self):
		return str(self.heap)