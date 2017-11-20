import unittest
from dlinkedlist import _DoublyLinkedBase


class Empty:
	""" Error when attempting to access elements of an empty container """
	pass


class LinkeDeque(_DoublyLinkedBase):
	"""
	Implementation of the Deque ADT
	Uses a doubly linked list for internal storage
	"""
	def first(self):
		""" Return the first element in the deck without removing it """
		if self.is_empty():
			raise Empty('Deque is empty')
		return self._header._next._element

	def last(self):
		""" Return last element in the deck without removig it """
		if self.is_empty():
			raise Empty('Deque is empty')
		return self._trailer._prev._element

	def add_first(self, e):
		""" Add an element to the front of the deck """
		self._insert_between(e, self._header, self._header._next)

	def add_last(self, e):
		""" Add an element to the back of the deck """
		self._insert_between(e, self._trailer._prev, self._trailer)

	def delete_first(self):
		""" Remove and return the element at the front of the deck """
		if self.is_empty():
			raise Empty('Deque is empty')
		return self._delete_node(self._header._next)

	def delete_last(self):
		""" Remove and return the element at the back of the deck """
		if self.is_empty():
			raise Empty('Deque is empty')
		return self._delete_node(self._trailer._prev)

class TestDeque(unittest.TestCase):

	def test_new_deque_is_empty(self):
		dq = LinkeDeque()
		self.assertTrue(dq.is_empty())
		self.assertEqual(len(dq), 0)

	def test_add_element_to_front_of_deque(self):
		dq = LinkeDeque()
		dq.add_first(1)
		self.assertFalse(dq.is_empty())
		self.assertEqual(len(dq), 1)

	def test_add_element_to_back_of_deque(self):
		dq = LinkeDeque()
		dq.add_last(1)
		self.assertFalse(dq.is_empty())
		self.assertEqual(len(dq), 1)

	def test_retrieve_first_element_in_deque(self):
		dq = LinkeDeque()
		dq.add_first(3)
		self.assertEqual(len(dq), 1)
		self.assertEqual(dq.first(), 3)

	def test_retrieve_last_element_in_deque(self):
		dq = LinkeDeque()
		dq.add_last(3)
		self.assertEqual(len(dq), 1)
		self.assertEqual(dq.last(), 3)
		self.assertEqual(len(dq), 1)

	def test_delete_first_element_in_deque(self):
		dq = LinkeDeque()
		dq.add_first(3)
		self.assertEqual(len(dq), 1)
		self.assertEqual(dq.delete_first(), 3)
		self.assertEqual(len(dq), 0)

	def test_delete_last_element_in_deque(self):
		dq = LinkeDeque()
		dq.add_last(3)
		self.assertEqual(len(dq), 1)
		self.assertEqual(dq.delete_last(), 3)
		self.assertEqual(len(dq), 0)

if __name__ == "__main__":
	unittest.main()
