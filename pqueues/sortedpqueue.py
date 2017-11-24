import sys
import unittest

sys.path.append("D:\\LEARN\\code\\msft\\linkedlists")
from positionlist import PositionList
from pqueuebase import PriorityQueueBase


class Empty(Exception):
	""" Raise error when attempting to retrieve item from an empty container """
	pass


class SortedPriorityQueue(PriorityQueueBase):
	""" A min-oriented priority queue implementation with an sorted position list """
	def __init__(self):
		""" Create a new empty Priority Queue """
		self._data = PositionList()

	def __len__(self):
		""" Return number of itemss in Priority Queue """
		return len(self._data)

	def add(self, key, value):
		""" Add a key-value pair to Priority Queue """
		newest = self._Item(key, value)
		walk = self._data.last() # start from the back
		while walk is not None and newest < walk.element():
			walk = self._data.before(walk)
		if walk is None:
			self._data.add_first(newest) # new item is the highest priority
		else:
			self._data.add_after(walk, newest)

	def min(self):
		""" Return a (key, value) tuple with minimum key, without removing it from Priority Queue """
		if self.is_empty():
			raise Empty('Priority Queue is empty')
		position = self._data.first()
		item = position.element()
		return ( item._key, item._value )

	def remove_min(self):
		""" Remove and return a (key, value) tuple with minimum key """
		if self.is_empty():
			raise Empty('Priority Queue is empty')
		position = self._data.first()
		item = self._data.delete(position)
		return ( item._key, item._value )


class TestPQueue(unittest.TestCase):
	def test_pqueue_empty_when_created(self):
		pq = SortedPriorityQueue()
		self.assertTrue(pq.is_empty())

	def test_add_item_to_pqueue(self):
		pq = SortedPriorityQueue()
		pq.add('A', 5)
		pq.add('B', 5)
		self.assertFalse(pq.is_empty())
		self.assertEqual(len(pq), 2)

	def test_retrieve_highest_prioroty_item(self):
		pq = SortedPriorityQueue()
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
