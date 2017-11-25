import unittest
from hashmapbase import HashMapBase
from unsortedtablemap import UnsortedTableMap


class ProbeHashMap(HashMapBase):
	""" Hash map with linear probing for collision resolution """
	_AVAIL = object() # a sentinel to marl positions of previous deletions

	def _is_available(self, j):
		""" Return true if index j is available """
		return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

	def _find_slot(self, j, key):
		"""
		Search a key in bucket at index j
		Returns (seccess, index) tuple i.e:
			(True, index) if match was found at index location
			(False, index) if match was not found and index is first available slot
		"""
		firstAvailable = None
		while True:
			if self._is_available(j):
				if firstAvailable is None:
					firstAvailable = j
				if self._table[j] is None:
					return (False, firstAvailable) # search failed
			elif key == self._table[j]._key:
				return (True, j) # found a match
			j = (j + 1) % len(self._table) # cyclic search

	def _bucket_getitem(self, j, key):
		""" Get an item associated with key from a bucket at index j of bucket array """
		found, index = self._find_slot(j, key)
		if not found:
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(key))
		return self._table[index]._value

	def _bucket_setitem(self, j, key, value):
		""" Set a key-value into bucket at index j of bucket array """
		found, index = self._find_slot(j, key)
		if not found: # store new key-value pair
			self._table[index] = self._Item(key, value)
			self._n += 1
		else: # update already existing
			self._table[index] = value

	def _bucket_delitem(self, j, key):
		""" Delete a key-value from bucket at index j of bucket array """
		found, index = self._find_slot(j, key)
		if not found:
			raise KeyError('Key Error: Map has no key-value entry for ' + repr(key))
		self._table[index] = ProbeHashMap._AVAIL # mark as formerly occupied

	def __iter__(self):
		""" A generator for all the keys in map """
		for j in range(len(self._table)):
			if not self._is_available(j):
				yield self._table[j]._key


class TestProbeHashMap(unittest.TestCase):

	def test_map_empty_on_initialization(self):
		m = ProbeHashMap()
		self.assertEqual(len(m), 0)

	def test_add_item_to_map(self):
		m = ProbeHashMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)

	def test_get_item_from_map(self):
		m = ProbeHashMap()
		m['key'] = 'value'
		self.assertEqual(m['key'], 'value')

	def test_get_item_not_in_map(self):
		m = ProbeHashMap()
		with self.assertRaisesRegex(KeyError, "Key Error: Map has no key-value entry for 'test'"):
			m['test']

	def test_delete_item_from_map(self):
		m = ProbeHashMap()
		m['key'] = 'value'
		self.assertEqual(len(m), 1)
		del m['key']
		self.assertEqual(len(m), 0)

	def test_iterate_over_map(self):
		m = ProbeHashMap()
		m['first'] = 1
		m['second'] = 2
		m['third'] = 3
		self.assertEqual( set(iter(m)), {'first', 'second', 'third'})

if __name__ == '__main__':
	unittest.main()
