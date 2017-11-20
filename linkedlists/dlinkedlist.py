import unittest


class Empty:
	""" Error when attempting to access elements of an empty container """
	pass


class _DoublyLinkedBase:
	""" A base class for a doubly linked list representation """
	class _Node:
		""" A non-public nested storage for a doubly linked node """
		__slots__ = '_element', '_next', '_prev' # streamline the memory
		def __init__(self, element, prev_, next_):
			"""
			Initialize a node
			element: reference to a users object
			next_: reference to the next node in doubly linked list
			prev_: reference to the previous node in a doubly linked list
			"""
			self._element = element
			self._prev = prev_
			self._next = next_

	def __init__(self):
		""" Create an empty list """
		self._header = self._Node(None, None, None)
		self._trailer = self._Node(None, None, None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		""" Return the numbe rof elements in the list """
		return self._size

	def is_empty(self):
		""" Return True if list is empty """
		return self._size == 0

	def _insert_between(self, e, predecessor, successor):
		""" Add an element between two existing nodes and return a new node """
		newest  = self._Node(e, predecessor, successor)
		predecessor._next = newest
		successor._prev = newest
		self._size += 1
		return newest

	def _delete_node(self, node):
		""" Delete a node and return its element, provided its not a sentinel """
		predecessor = node._prev
		successor = node._next

		if predecessor and successor: #ensure node is not a sentinel
			predecessor._next = successor
			successor._prev = predecessor
			self._size -= 1
			element = node._element
			node._prev = node._next = node._element = None # cleanup
			return element
		raise Exception('You can not delete a sentinel node!')


class TestList(unittest.TestCase):

	def test_base_list_empty_when_created(self):
		bl = _DoublyLinkedBase()
		self.assertTrue(bl.is_empty())
		self.assertEqual(len(bl), 0)

	def test_insert_elements_to_base_list(self):
		bl = _DoublyLinkedBase()
		first = bl._insert_between('First', bl._header, bl._trailer)
		self.assertFalse(bl.is_empty())
		self.assertEqual(len(bl), 1)
		self.assertEqual(first, bl._trailer._prev)
		second = bl._insert_between('Second', first, bl._trailer)
		self.assertEqual(len(bl), 2)
		self.assertEqual(second, bl._header._next._next)
		self.assertEqual(second, bl._trailer._prev)

	def test_delete_nodes(self):
		bl = _DoublyLinkedBase()
		first = bl._insert_between('First', bl._header, bl._trailer)
		second = bl._insert_between('Second', first, bl._trailer)
		self.assertEqual(len(bl), 2)
		self.assertEqual(bl._delete_node(first), 'First')
		self.assertEqual(len(bl), 1)
		self.assertEqual(bl._header._next, second)
		self.assertEqual(bl._delete_node(second), 'Second')
		self.assertTrue(bl.is_empty())
		with self.assertRaisesRegex(Exception, 'You can not delete a sentinel node!'):
			bl._delete_node(bl._header)
		with self.assertRaisesRegex(Exception, 'You can not delete a sentinel node!'):
			bl._delete_node(bl._trailer)


if __name__ == '__main__':
	unittest.main()
