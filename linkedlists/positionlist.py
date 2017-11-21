import unittest
from dlinkedlist import _DoublyLinkedBase

class PositionList(_DoublyLinkedBase):
	""" A sequential container of elements allowing positional access """
	class Position:
		"""
		Nested public position class
		Abstracts the representation of location of a single element
		"""
		def __init__(self, container, node):
			""" Constructor should never be invoked by user """
			self._container = container
			self._node = node

		def element(self):
			""" Return the element stored at this position """
			return self._node._element

		def __eq__(self, other):
			""" Return True if both reference the same location """
			return type(other) is type(self) and other._node is self._node

		def __ne__(self, other):
			""" Return True if other doesn't reference the same location """
			return not( self == other)

	def _validate(self, p):
		""" Utility: Return positions' node or raise appropriate error if invalid """
		if not isinstance(p, self.Position): # p not a list position
			raise TypeError('p must be proper Position type')
		if p._container is not self: # p from different list
			raise ValueError('p does not belong to this container')
		if p._node._next is None: # deprecated nodes
			raise ValueError('p is no longer valid')
		return p._node

	def _make_position(self, node):
		""" Utility: Return Position instance for given node (None if node is a sentinel) """
		if node is self._header or node is self._trailer:
			return None
		return self.Position(self, node)

	# Accessor methods ---------------------------------------------

	def first(self):
		""" Return the first Position in list, None if list is empty """
		return self._make_position(self._header._next)

	def last(self):
		""" Return the last Position in list, None if list is empty """
		return self._make_position(self._trailer._prev)

	def before(self, p):
		""" Return the Position just before p, None if p is the first """
		node = self._validate(p)
		return self._make_position(node._prev)

	def after(self, p):
		""" Return the Position just after p, None if p is the last """
		node = self._validate(p)
		return self._make_position(node._next)

	def __iter__(self):
		""" Generate a foward iterator of elements in the list """
		cursor = self.first()
		while cursor is not None:
			yield cursor.element()
			cursor = self.after(cursor)

	# Mutator methods ---------------------------------------------

	def _insert_between(self, e, predecessor, successor):
		"""
		Add element between existing nodes and return new Position
		Overrides inherited version to return Position rather than Node
		"""
		node = super()._insert_between(e, predecessor, successor)
		return self._make_position(node)

	def add_first(self, e):
		""" Insert element e at the front of list and return new Position """
		return self._insert_between(e, self._header, self._header._next)

	def add_last(self, e):
		""" Insert element e at the back of list and return new Position """
		return self._insert_between(e, self._trailer._prev, self._trailer)

	def add_before(self, p, e):
		""" Insert element e into list before Position p and return rew Position """
		node = self._validate(p)
		return self._insert_between(e, node._prev, node)

	def add_after(self, p, e):
		""" Insert element e into list after Position p and return new Positio """
		node = self._validate(p)
		return self._insert_between(e, node, node._next)

	def delete(self, p):
		""" Remove and return element at Position p """
		node = self._validate(p)
		return self._delete_node(node)

	def replace(self, p, e):
		""" Replace element at Position p and return the value replaced """
		node = self._validate(p)
		original_value = node._element
		node._element = e
		return original_value


class TestPositionList(unittest.TestCase):
	def test_new_list_empty_when_created(self):
		pl = PositionList()
		self.assertTrue(pl.is_empty())

	def test_add_element_to_front_of_list(self):
		pl = PositionList()
		first = pl.add_first(30)
		self.assertEqual(pl.first(), first)
		self.assertEqual(first.element(), 30)

	def test_add_element_to_back_of_luist(self):
		pl = PositionList()
		last = pl.add_last(300)
		self.assertEqual(pl.last(), last)
		self.assertEqual(last.element(), 300)

	def test_first_equal_last(self):
		pl = PositionList()
		posn = pl.add_first(150)
		self.assertEqual(pl.first(), pl.last())
		self.assertEqual(pl.first().element(), pl.last().element())

	def test_add_first_and_last(self):
		pl = PositionList()
		posn = pl.add_first(150)
		posn2 = pl.add_last(15)
		self.assertNotEqual(pl.first(), pl.last())
		self.assertNotEqual(pl.first().element(), pl.last().element())

	def test_add_before(self):
		pl = PositionList()
		first = pl.add_first(10)
		self.assertEqual(pl.first().element(), 10)
		pl.add_before(first, 0)
		self.assertEqual(pl.first().element(), 0)

	def test_add_after(self):
		pl = PositionList()
		last = pl.add_last(10)
		self.assertEqual(pl.last().element(), 10)
		pl.add_after(last, 100)
		self.assertEqual(pl.last().element(), 100)

	def test_delete_element(self):
		pl = PositionList()
		posn = pl.add_first(100)
		self.assertFalse(pl.is_empty())
		self.assertEqual(pl.delete(posn), 100)
		self.assertTrue(pl.is_empty())

	def test_replace_element(self):
		pl = PositionList()
		posn = pl.add_last(100)
		self.assertEqual(posn.element(), 100)
		self.assertEqual(pl.replace(posn, 200), 100)
		self.assertEqual(posn.element(), 200)

	def test_before_accessor(self):
		pl = PositionList()
		first = pl.add_first(10)
		self.assertEqual(pl.before(first), None)
		last = pl.add_last(20)
		self.assertEqual(pl.before(last), first)

	def test_after_accessor(self):
		pl = PositionList()
		last = pl.add_last(20)
		self.assertEqual(pl.after(last), None)
		first = pl.add_first(10)
		self.assertEqual(pl.after(first), last)

	def test_iterate_over_lists(self):
		pl = PositionList()
		first = pl.add_first(10)
		pl.add_after(first, 20)
		last = pl.add_last(40)
		pl.add_before(last, 30)
		self.assertEqual(list(iter(pl)), [10, 20, 30, 40])


if __name__ == '__main__':
	unittest.main()
