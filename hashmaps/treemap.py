import sys
import unittest

sys.path.append('D:\\LEARN\\code\msft\\trees')
from linkedbinarytree import LinkedBinaryTree
from mapbase import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
	""" A sorted map using a Binary Search Tree """
	class Position(LinkedBinaryTree.Position):
		""" Override the position class """
		def key(self):
			""" Return key of a map's key-value pair """
			return self.element()._key

		def value(self):
			""" Return value of a map's key-value pair """
			return self.element()._value

	# Non-public utilities -------------------

	def _subtree_search(self, p, k):
		"""
		Return position of p's subtree having key k
		If not found, return last node searched
		"""
		if k == p.key():
			return p
		elif k < p.key():
			if self.left(p) is not None: # search left subtree
				return self._subtree_search(self.left(p), k)
		else:
			if self.right(p) is not None: # search right subtree
				return self._subtree_search(self.right(p), k)
		return p # not found: return last position searched

	def _subtree_first_position(self, p):
		""" Return position of first item on subtree rooted at p """
		walk = p
		while self.left(walk) is not None:
			walk = self.left(walk)
		return walk

	def _subtree_last_position(self, p):
		""" Return position of last item on subtree rooted at p """
		walk = p
		while self.right(walk) is not None:
			walk = self.right(walk)
		return walk

	# Public accesor utilities ---------------

	def is_empty(self):
		""" Return True if map has no elements """
		return self._size == 0

	def first(self):
		""" Return the first position in tree, None if map is empty """
		return self._subtree_first_position(self.root()) if len(self) > 0 else None

	def last(self):
		""" Return the last position in tree , None if map is empty """
		return self._subtree_last_position(self.root()) if len(self) > 0 else None

	def before(self, p):
		""" Return position just before p in natural order, None if p is first position """
		self._validate(p)
		if self.left(p) is not None:
			return self._subtree_last_position(self.left(p))
		else:
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.left(above):
				walk = above
				above = self.parent(walk)
			return above

	def after(self, p):
		""" Return position just after p in natural order, None if p is last position """
		self._validate(p)
		if self.right(p) is not None:
			return self._subtree_first_position(self.right(p))
		else:
			walk = p
			above = self.parent(walk)
			while above is not None and walk == self.right(above):
				walk = above
				above = self.parent(walk)
			return walk

	def find_position(self, k):
		""" Return position with key k, else return its Neighbor, else return None """
		if self.is_empty():
			return  None
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p) # hook for balanced tree subclasses
			return p

	def find_min(self):
		""" Return (key, value) pair with minimum key, None if map is empty """
		if self.is_empty():
			return None
		else:
			p = self.first()
			return (p.key(), p.value())

	def find_max(self):
		""" Return (key, value) pair with maximum key, None if map is empty """
		if self.is_empty():
			return None
		else:
			p = self.last()
			return (p.key(), p.value())

	def find_ge(self, k):
		""" Return (key, value) pair with least key greater than or equal to k else None """
		if self.is_empty():
			return None
		else:
			p = self.find_position(k)
			if p.key() < k:
				p.self.after(p)
			return (p.key(), p.value()) if p is not None else p

	def find_range(self, start=None, stop=None):
		"""
		Iterate all (key, value) pairs such that start <= key < stop
		Iteration begins with min key of map if start is None
		Iteration continues through last key on map if stop is None
		"""
		if not self.is_empty():
			if start is None:
				p = self.first()
			else:
				p = self.find_position(start)
				if p.key() < start:
					p = self.after(p)
			while p is not None and (stop is None or p.key() < stop):
				yield (p.key(), p.value())
				p.self.after(p)

	def __getitem__(self, k):
		""" Return a value associated with key k else raise Key Error if not in map """
		if self.is_empty():
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(k))
		else:
			p = self._subtree_search(self.root(), k)
			self._rebalance_access(p)
			if k != p.key():
				raise KeyError('Key Error: Map has no key-value entry for ' + repr(k))
			return p.value()

	def __setitem__(self, k, v):
		""" Assign value v to key k, overwriting existing value if already present """
		if self.is_empty():
			leaf = self._add_root(self._Item(k, v))
		else:
			p = self._subtree_search(self.root(), k)
			if p.key() == k:
				p.element()._value = v # replace existing items value
				self._rebalance_access(p)
				return
			else:
				item = self._Item(k, v)
				if p.key() < k:
					leaf = self._add_right(p, item)
				else:
					leaf = self._add_left(p, item)
		self._rebalance_access(leaf)


	def __iter__(self):
		""" Generate an iteration of all keys in the map in order """
		p = self.first()
		while p is not None:
			yield p.key()
			p = self.after(p)

	def delete(self, p):
		""" Remove the item at given position """
		self._validate(p)
		if self.left(p) and self.right(p):
			replacement = self._subtree_last_position(self.left(p))
			self._replace(p, replacement.element())
			p = replacement
		parent = self.parent(p)
		self._delete(p)
		self._rebalance_delete(parent)

	def __delitem__(self, k):
		""" Remove item associated with key k, raise Key Error if not found """
		if self.is_empty():
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(k))
		else:
			p = self._subtree_search(self.root(), k)
			if k == p.key():
				self.delete(p)
				return
			self._rebalance_access(p)


class TestTreeMap(unittest.TestCase):

	def test_map_empty_on_initialization(self):
		m = TreeMap()
		self.assertEqual(len(m), 0)

	def test_add_item_to_map(self):
		m = TreeMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)

	def test_get_item_from_map(self):
		m = TreeMap()
		m['key'] = 'value'
		self.assertEqual(m['key'], 'value')

	def test_get_item_not_in_map(self):
		m = TreeMap()
		with self.assertRaisesRegex(KeyError, "Key Error: Map has no key-value entry for 'test'"):
			m['test']

	def test_find_minimum(self):
		m = TreeMap()
		self.assertEqual(m.find_min(), None)
		m['A'] = 'a'
		m['B'] = 'b'
		self.assertEqual(m.find_min(), ('A', 'a'))

	def test_find_maximum(self):
		m = TreeMap()
		self.assertEqual(m.find_max(), None)
		m['A'] = 'a'
		m['B'] = 'b'
		self.assertEqual(m.find_max(), ('B', 'b'))

	def test_find_less_than(self):
		m = TreeMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		self.assertEqual(m.find_lt('C'), ('B', 'b'))
		self.assertEqual(m.find_lt('A'), None)

	def test_find_less_than_or_equal_to(self):
		m = TreeMap()
		m['A'] = 'a'
		m['B'] = 'b'
		self.assertEqual(m.find_le('A'), ('A', 'a'))
		self.assertEqual(m.find_le('C'), ('B', 'b'))

	def test_find_greater_than(self):
		m = TreeMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		self.assertEqual(m.find_gt('A'), ('B', 'b'))
		self.assertEqual(m.find_gt('C'), None)

	def test_find_greater_than_or_equal_to(self):
		m = TreeMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		self.assertEqual(m.find_ge('A'), ('A', 'a'))
		self.assertEqual(m.find_ge('C'), ('C', 'c'))

	def test_get_range(self):
		m = TreeMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		m['D'] = 'd'
		self.assertEqual(list(m.find_range('A', 'C')), [('A', 'a'), ('B', 'b')])
		self.assertEqual(list(m.find_range('E', 'F')), [])

	def test_delete_item_from_map(self):
		m = TreeMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)
		del m['key']
		self.assertEqual(len(m), 0)

	def test_iterate_over_map(self):
		m = TreeMap()
		m['first'] = 1
		m['second'] = 2
		m['third'] = 3
		self.assertEqual( set(iter(m)), {'first', 'second', 'third'})

	def test_order_of_items_in_map(self):
		m = TreeMap()
		m['D'] = 'd'
		m['B'] = 'b'
		m['C'] = 'c'
		m['A'] = 'a'
		self.assertEqual( list(iter(m)), ['A', 'B', 'C', 'D'])

if __name__ == '__main__':
	unittest.main()
