import unittest
from heapqueue import HeapPriorityQueue


class Empty(Exception):
	""" Raise error when attempting to retrieve item from an empty container """
	pass


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
	"""	An adaptable locator based priority queue implemented with the binary heap """

	class Locator(HeapPriorityQueue._Item):
		""" Locator class: Token for locating an entry of the priority queue """
		__slots__ = '_index' # streamline memory

		def __init__(self, key, value, index):
			""" Instantiate a new Locator instance """
			super().__init__(key, value)
			self._index = index

	# Non-public behaviors ----------------------

	def _swap(self, i, j):
		"""
		Override swap functionality
		records new indices
		"""
		super()._swap(i, j)
		self._data[i]._index = i # reset the locator indices after swap
		self._data[j]._index = j

	def _bubble(self, j):
		""" Reassert heap order property """
		if j > 0 and self._data[j] < self._data[self._parent(j)]:
			self._upheap(j)
		else:
			self._downheap(j)

	# Public behaviors ------------------------

	def add(self, key, value):
		""" Add a key-value pair to heap """
		token = self.Locator(key, value, len(self._data)) # initialize new locator index
		self._data.append(token)
		self._upheap(len(self._data) - 1)
		return token

	def update(self, loc, newkey, newvalue):
		""" Update the key and value for the entry identified by Locator loc """
		j = loc._index
		if not(0 <= j < len(self) and self._data[j] is loc) \
			or not isinstance(loc, self.Locator):
			raise ValueError('Invalid locator')
		loc._key = newkey
		loc._value = newvalue
		self._bubble(j)

	def remove(self, loc):
		""" Remove and return (key, value) tuple identified by Locator loc """
		j = loc._index
		if not(0 <= j < len(self) and self._data[j] is loc) \
			or not isinstance(loc, self.Locator):
			raise ValueError('Invalid locator')
		if j == len(self) - 1: # element at the last position
			self._data.pop()
		else:
			self._swap(j, len(self) - 1)
			self._data.pop()
			self._bubble(j)
		return(loc._key, loc._value)

class TestPQueue(unittest.TestCase):
	def test_pqueue_empty_when_created(self):
		pq = AdaptableHeapPriorityQueue()
		self.assertTrue(pq.is_empty())

	def test_add_item_to_pqueue(self):
		pq = AdaptableHeapPriorityQueue()
		pq.add('A', 5)
		pq.add('B', 5)
		self.assertFalse(pq.is_empty())
		self.assertEqual(len(pq), 2)

	def test_retrieve_highest_prioroty_item(self):
		pq = AdaptableHeapPriorityQueue()
		pq.add('P', 100)
		pq.add('B', 30)
		pq.add('A', 1000)
		self.assertEqual(pq.min(), ('A', 1000))
		self.assertEqual(len(pq), 3)
		self.assertEqual(pq.remove_min(), ('A', 1000))
		self.assertEqual(len(pq), 2)
		self.assertEqual(pq.remove_min(), ('B', 30))

	def test_locations(self):
		"""
		Adding an element returns its location

		Locations are in order of nonincreasing priority
		Expected order of priority below: c, a, b
		a,b,c are locators::
		"""
		pq = AdaptableHeapPriorityQueue()
		a = pq.add('B', 100) # loc 2,
		b = pq.add('C', 30) #loc 1
		c = pq.add('A', 1000) #loc o
		self.assertLess(c, a)
		self.assertGreater(b, a)

	def test_update_item_at_location(self):
		pq = AdaptableHeapPriorityQueue()
		a = pq.add('B', 100) # loc 2,
		b = pq.add('C', 30) #loc 1
		c = pq.add('A', 1000) #loc o
		self.assertEqual(pq.min(), ('A', 1000))
		pq.update(c, 'A', 500)
		self.assertEqual(pq.min(), ('A', 500))
		pq.update(c, 'D', 500)
		self.assertEqual(pq.min(), ('B', 100))

	def test_remove_item_at_location(self):
		pq = AdaptableHeapPriorityQueue()
		a = pq.add('B', 100) # loc 2,
		b = pq.add('C', 30) #loc 1
		c = pq.add('A', 1000) #loc o
		self.assertEqual(pq.remove(b), ('C', 30))
		self.assertEqual(len(pq), 2)
		self.assertEqual(pq.remove(c), ('A', 1000))
		self.assertEqual(len(pq), 1)
		self.assertEqual(pq.min(), ('B', 100))

if __name__ == '__main__':
	unittest.main()
