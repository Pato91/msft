import unittest
from pqueuebase import PriorityQueueBase


class Empty(Exception):
	""" Raise error when attempting to retrieve item from an empty container """
	pass


class HeapPriorityQueue(PriorityQueueBase):
	"""
	A min-oriented priority queue implementation witha binary heap
	Binary Heap is based on an array structure mimicing a binary tree
	"""

	# Non-public behaviors ----------------------

	def _parent(self, j):
		return (j-1) // 2

	def _left(self, j):
		return 2*j + 1

	def _right(self, j):
		return 2*j + 2

	def _has_left(self, j):
		return self._left(j) < len(self._data) # index beyond end of list ?

	def _has_right(self, j):
		return self._right(j) < len(self._data) # index beyond end of list ?

	def _swap(self, i, j):
		""" Swap the elements at indices i and j of array """
		self._data[i], self._data[j] = self._data[j], self._data[i]

	def _upheap(self, j):
		""" Bubble a position up the heap """
		parent = self._parent(j)
		if j > 0 and self._data[j] < self._data[parent]:
			self._swap(j, parent)
			self._upheap(parent)

	def _downheap(self, j):
		""" Bubble a position down the heap """
		if self._has_left(j):
			left = self._left(j)
			small_child = left
			if self._has_right(j):
				right = self._right(j)
				if self._data[right] < self._data[small_child]:
					small_child = right
			if self._data[small_child] < self._data[j]:
				self._swap(j, small_child)
				self._downheap(small_child)

	# Public behaviors ------------------------

	def __init__(self):
		""" Create a new empty Priority Queue """
		self._data = []

	def __len__(self):
		"""Return the number of items in priority queue """
		return len(self._data)

	def add(self, key, value):
		""" Add a key-value pair to priority queue """
		self._data.append(self._Item(key, value))
		self._upheap(len(self._data) - 1)

	def min(self):
		""" Return a (key, value) tuple with minimum key, but dont remove from queue """
		if self.is_empty():
			raise Empty('Priority Queue is empty')
		item = self._data[0]
		return (item._key, item._value)

	def remove_min(self):
		""" Remove and return (key, value) pair with the least key """
		if self.is_empty():
			raise Empty('Priority Queue is empty')
		self._swap(0, len(self._data) - 1)
		item = self._data.pop()
		self._downheap(0)
		return (item._key, item._value)


class TestPQueue(unittest.TestCase):
	def test_pqueue_empty_when_created(self):
		pq = HeapPriorityQueue()
		self.assertTrue(pq.is_empty())

	def test_add_item_to_pqueue(self):
		pq = HeapPriorityQueue()
		pq.add('A', 5)
		pq.add('B', 5)
		self.assertFalse(pq.is_empty())
		self.assertEqual(len(pq), 2)

	def test_retrieve_highest_prioroty_item(self):
		pq = HeapPriorityQueue()
		pq.add('P', 100)
		pq.add('B', 30)
		pq.add('A', 1000)
		self.assertEqual(pq.min(), ('A', 1000))
		self.assertEqual(len(pq), 3)
		self.assertEqual(pq.remove_min(), ('A', 1000))
		self.assertEqual(len(pq), 2)
		self.assertEqual(pq.remove_min(), ('B', 30))

if __name__ == '__main__':
	unittest.main()
