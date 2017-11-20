import unittest

class Empty:
	"""Error attempting to access an element from an empty container"""
	pass


class CircularQueue:
	"""
	FIFO Implementation of a queue ADT
	uses a circularly linked list for underlying storage

	Round-Robin scheduler implementation
	"""
	class _Node:
		""" A non-public nested storage for a circularly linked list """
		__slots__ = '_element', '_next' # streamline the memory
		def __init__(self, element, next_):
			"""
			Initialize a node
			element: reference to a users object
			next_: reference to the next node in linked list
			"""
			self._element = element
			self._next = next_

	def __init__(self):
		""" Create an empty queue """
		self._tail = None
		self._size = 0

	def __len__(self):
		""" Return the size of the queue """
		return self._size

	def is_empty(self):
		""" Returns true if queue is empty """
		return self._size == 0

	def first(self):
		""" Return the first element in the queue without removing it """
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		return head._element

	def dequeue(self):
		""" Remove and return the first element in the queue """
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = head._next
		self._size -= 1
		return head._element

	def enqueue(self, e):
		""" Add element to the back of the queue """
		newest = self._Node(e, None)
		if self.is_empty():
			newest._next = newest # head is the tail, circular
		else:
			newest._next = self._tail._next
			self._tail._next = newest
		self._tail = newest
		self._size += 1

	def rotate(self):
		""" Rotate front element to the back of the queue """
		if self._size > 0:
			self._tail = self._tail._next

class TestQueue(unittest.TestCase):

	def test_new_queue_is_empty(self):
		q = CircularQueue()
		self.assertTrue(q.is_empty())
		self.assertEqual(len(q), 0)

	def test_add_element_to_queue(self):
		q= CircularQueue()
		q.enqueue(1)
		self.assertFalse(q.is_empty())
		self.assertEqual(len(q), 1)

	def test_queue_is_strictly_FIFO(self):
		q = CircularQueue()
		q.enqueue(1)
		q.enqueue(2)
		self.assertEqual(len(q), 2)
		self.assertEqual(q.dequeue(), 1)
		self.assertEqual(len(q), 1)

	def test_retrieve_first_element_in_queue(self):
		q= CircularQueue()
		q.enqueue(3)
		self.assertEqual(len(q), 1)
		self.assertEqual(q.first(), 3)
		self.assertEqual(len(q), 1)

	def test_rotate_queue(self):
		q= CircularQueue()
		q.enqueue(1)
		q.enqueue(2)
		self.assertEqual(len(q), 2)
		self.assertEqual(q.first(), 1)
		q.rotate()
		self.assertEqual(q.first(), 2)
		self.assertEqual(len(q), 2)


	def test_service_queue(self):
		def service(e):
			""" service an element
			add two to number and return
			"""
			return e + 2

		q= CircularQueue()
		q.enqueue(1)
		q.enqueue(2)
		self.assertEqual(q.first(), 1)
		serviced = service(q.dequeue()) # 2+1 = 3
		q.enqueue(serviced)
		self.assertEqual(q.first(), 2)
		serviced = service(q.dequeue()) # 2+2 = 4
		q.enqueue(serviced)
		self.assertEqual(q.first(), 3)
		q.rotate()
		self.assertEqual(q.first(), 4)

if __name__ == "__main__":
	unittest.main()
