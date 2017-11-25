import unittest
from mapbase import MapBase


class UnsortedTableMap(MapBase):
	"""
	Simple map implementation using an unordered list
	Inneficient: worst case lookups in O(n) - linear time
	"""
	def __init__(self):
		""" Create an empty map """
		self._table = []

	def __getitem__(self, key):
		""" Return a value associated with key k from map, raise KeyError if not found """
		for item in self._table: # O(n) worst case
			if key == item._key:
				return item._value
		raise KeyError('Key Error: Map has no key-value entry for '+ repr(key))

	def __setitem__(self, key, value):
		""" Assign value to key, overwriting current value if key already present in map"""
		for item in self._table:
			if key == item._key: # key already in table
				item._value = value
				return
		self._table.append(self._Item(key, value)) # add new key to table

	def __delitem__(self, key):
		""" Remove an item associated with key from map, raise KeyError if not found """
		for i in range(len(self._table)):
			if key == self._table[i]._key:
				self._table.pop(i)
				return
		raise KeyError('Key Error: Map has no key-value entry for ' + repr(key))

	def __len__(self):
		""" Return the number of items in map """
		return len(self._table)

	def __iter__(self):
		""" Return a generator of map keys """
		for item in self._table:
			yield item._key


class TestUnsortedTableMap(unittest.TestCase):

	def test_map_empty_on_initialization(self):
		m = UnsortedTableMap()
		self.assertEqual(len(m), 0)

	def test_add_item_to_map(self):
		m = UnsortedTableMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)

	def test_get_item_from_map(self):
		m = UnsortedTableMap()
		m['key'] = 'value'
		self.assertEqual(m['key'], 'value')

	def test_get_item_not_in_map(self):
		m = UnsortedTableMap()
		with self.assertRaisesRegex(KeyError, "Key Error: Map has no key-value entry for 'test'"):
			m['test']

	def test_delete_item_from_map(self):
		m = UnsortedTableMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)
		del m['key']
		self.assertEqual(len(m), 0)

	def test_iterate_over_map(self):
		m = UnsortedTableMap()
		m['first'] = 1
		m['second'] = 2
		m['third'] = 3
		self.assertEqual( set(iter(m)), {'first', 'second', 'third'})

if __name__ == '__main__':
	unittest.main()
