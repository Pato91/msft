import unittest
from mapbase import MapBase

class SortedTableMap(MapBase):
	""" Map implementation using a sorted table """

	# Non-public behaviors ----------------

	def _find_index(self, k, low, high):
		"""
		Return index of the leftmost item with key >= k
		Return a j which is high + 1 if no such item exists
		Implication: j is returned such that:
			all items of slice table[low:j] have key < k
			all items of slice table[j:high+1] have key >= k
		"""
		# binary search
		if high < low:
			return high + 1
		else:
			mid = (low + high) // 2
			if k == self._table[mid]._key:
				return mid
			elif k < self._table[mid]._key:
				return self._find_index(k, low, mid-1)
			else:
				return self._find_index(k, mid+1, high)

	# Public behaviors -------------------

	def __init__(self):
		""" Create an empty map """
		self._table = []

	def __len__(self):
		""" Return number of items in the map """
		return len(self._table)

	def __getitem__(self, k):
		""" Return value associated with key k, raise KeyError if key not found in map """
		j = self._find_index(k, 0, len(self._table) - 1)
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(k))
		return self._table[j]._value

	def __setitem__(self, k, v):
		""" Assign a value v to key k, overwriting value if key already present in map """
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			self._table[j]._value = v # update value
		else:
			self._table.insert(j, self._Item(k, v)) # insert new key-value

	def __delitem__(self, k):
		""" Remove item associated with key k from map, raise KeyError if key not in map """
		j = self._find_index(k, 0, len(self._table) - 1)
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(k))
		else:
			self._table.pop(j)

	def __iter__(self):
		""" Generate keys of the map ordered from minimum to maximum: natural order """
		for item in self._table:
			yield item._key

	def __reversed__(self):
		""" Generate keys of the map ordered from maximum to minimum: reverse order """
		for item in reversed(self._table):
			yield item._key

	def find_min(self):
		""" Return (key, value) pair with minimum key, None if map is empty """
		if len(self._table) > 0:
			return (self._table[0]._key, self._table[0]._value)
		return None

	def find_max(self):
		""" Return (key, value) pair with maximum key, None if map is empty """
		if len(self._table) > 0:
			return (self._table[-1]._key, self._table[-1]._value)
		return None

	def find_ge(self, k):
		""" Return (key, value) pair with least key greater than or equal to k """
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table):
			return (self._table[j]._key, self._table[j]._value)
		return None

	def find_gt(self, k):
		""" Return (key, value) pair with least key strictly greater than k """
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			j += 1
		if j < len(self._table):
			return (self._table[j]._key, self._table[j]._value)
		return None

	def find_le(self, k):
		""" Return (key, value) pair with maximum key less than or equal to k """
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k: # 'equal-to' case
			return (self._table[j]._key, self._table[j]._value)
		elif j > 0: # 'less-than' case
			return (self._table[j-1]._key, self._table[j-1]._value)
		return None

	def find_lt(self, k):
		""" Return (key, value) pair with maximum key strictly less than k """
		j = self._find_index(k, 0, len(self._table) - 1)
		if j > 0:
			return (self._table[j-1]._key, self._table[j-1]._value)
		return None

	def find_range(self, start, stop):
		"""
		Iterate all (key, value) pairs such that  start <= key < stop
		Iteration begins with minimum key of map if start is None
		Iteration ends with maximum key of map if stop is None
		"""
		j = 0 if start is None else self._find_index(start, 0, len(self._table) - 1)
		while j < len(self._table) and (stop is None or self._table[j]._key < stop):
			yield (self._table[j]._key, self._table[j]._value)
			j += 1


class TestSortedTableMap(unittest.TestCase):

	def test_map_empty_on_initialization(self):
		m = SortedTableMap()
		self.assertEqual(len(m), 0)

	def test_add_item_to_map(self):
		m = SortedTableMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)

	def test_get_item_from_map(self):
		m = SortedTableMap()
		m['key'] = 'value'
		self.assertEqual(m['key'], 'value')

	def test_get_item_not_in_map(self):
		m = SortedTableMap()
		with self.assertRaisesRegex(KeyError, "Key Error: Map has no key-value entry for 'test'"):
			m['test']

	def test_find_minimum(self):
		m = SortedTableMap()
		self.assertEqual(m.find_min(), None)
		m['A'] = 'a'
		m['B'] = 'b'
		self.assertEqual(m.find_min(), ('A', 'a'))

	def test_find_maximum(self):
		m = SortedTableMap()
		self.assertEqual(m.find_max(), None)
		m['A'] = 'a'
		m['B'] = 'b'
		self.assertEqual(m.find_max(), ('B', 'b'))

	def test_find_less_than(self):
		m = SortedTableMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		self.assertEqual(m.find_lt('C'), ('B', 'b'))
		self.assertEqual(m.find_lt('A'), None)

	def test_find_less_than_or_equal_to(self):
		m = SortedTableMap()
		m['A'] = 'a'
		m['B'] = 'b'
		self.assertEqual(m.find_le('A'), ('A', 'a'))
		self.assertEqual(m.find_le('C'), ('B', 'b'))

	def test_find_greater_than(self):
		m = SortedTableMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		self.assertEqual(m.find_gt('A'), ('B', 'b'))
		self.assertEqual(m.find_gt('C'), None)

	def test_find_greater_than_or_equal_to(self):
		m = SortedTableMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		self.assertEqual(m.find_ge('A'), ('A', 'a'))
		self.assertEqual(m.find_ge('C'), ('C', 'c'))

	def test_get_range(self):
		m = SortedTableMap()
		m['A'] = 'a'
		m['B'] = 'b'
		m['C'] = 'c'
		m['D'] = 'd'
		self.assertEqual(list(m.find_range('A', 'C')), [('A', 'a'), ('B', 'b')])
		self.assertEqual(list(m.find_range('E', 'F')), [])

	def test_delete_item_from_map(self):
		m = SortedTableMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)
		del m['key']
		self.assertEqual(len(m), 0)

	def test_iterate_over_map(self):
		m = SortedTableMap()
		m['first'] = 1
		m['second'] = 2
		m['third'] = 3
		self.assertEqual( set(iter(m)), {'first', 'second', 'third'})

	def test_order_of_items_in_map(self):
		m = SortedTableMap()
		m['D'] = 'd'
		m['B'] = 'b'
		m['C'] = 'c'
		m['A'] = 'a'
		self.assertEqual( list(iter(m)), ['A', 'B', 'C', 'D'])

if __name__ == '__main__':
	unittest.main()
