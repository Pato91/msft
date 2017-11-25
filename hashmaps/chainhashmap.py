import unittest
from hashmapbase import HashMapBase
from unsortedtablemap import UnsortedTableMap


class ChainHashMap(HashMapBase):
	""" Hash map with separate chaining for collision resolution """

	def _bucket_getitem(self, j, key):
		""" Get an item associated with key from a bucket at index j of bucket array """
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(key))
		return bucket[key]

	def _bucket_setitem(self, j, key, value):
		""" Set a key-value into bucket at index j of bucket array """
		if self._table[j] is None:
			self._table[j] = UnsortedTableMap()
		oldsize = len(self._table[j])
		self._table[j][key] = value
		if len(self._table[j]) > oldsize: # new item just added (increase size as below)
			self._n += 1

	def _bucket_delitem(self, j, key):
		""" Delete a key-value from bucket at index j of bucket array """
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(key))
		try:
			del bucket[key]
		except KeyError:
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(key))

	def __iter__(self):
		""" A generator for all the keys in map """
		for bucket in self._table:
			if bucket is not None:
				for key in bucket:
					yield key


class TestChainHashMap(unittest.TestCase):

	def test_map_empty_on_initialization(self):
		m = ChainHashMap()
		self.assertEqual(len(m), 0)

	def test_add_item_to_map(self):
		m = ChainHashMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)

	def test_get_item_from_map(self):
		m = ChainHashMap()
		m['key'] = 'value'
		self.assertEqual(m['key'], 'value')

	def test_get_item_not_in_map(self):
		m = ChainHashMap()
		with self.assertRaisesRegex(KeyError, "Key Error: Map has no key-value entry for 'test'"):
			m['test']

	def test_delete_item_from_map(self):
		m = ChainHashMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)
		del m['key']
		self.assertEqual(len(m), 0)

	def test_iterate_over_map(self):
		m = ChainHashMap()
		m['first'] = 1
		m['second'] = 2
		m['third'] = 3
		self.assertEqual( set(iter(m)), {'first', 'second', 'third'})

if __name__ == '__main__':
	unittest.main()
