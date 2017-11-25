import unittest



class MultiMap:
	"""
	A multimap class built upon use of an underlying map for storage
	Storage implementation can be switched by changing Map-Type below
	"""
	_MapType = dict # can be redefined by subclas

	def __init__(self):
		""" Instantiate a new empty multimap """
		self._map = self._MapType()
		self._n = 0 # count of items in map

	def __iter__(self):
		""" Iterate through all (key, value) pairs in multimap """
		for key, secondary in self._map.items():
			for value in secondary:
				yield (key, value)

	def __len__(self):
		""" return the count of items in multimap """
		return self._n

	def add(self, key, value):
		""" Add (key, value) pair to multimap """
		container = self._map.setdefault(key, []) # creates empty list if needed
		container.append(value)
		self._n += 1

	def pop(self, key):
		""" Remove and return arbitrary (key, value) or raise KeyError if key not in multimap """
		try:
			secondary = self._map[key]
			value = secondary.pop()
			if len(secondary) == 0: # no more pairs for key
				del self._map[key]
			self._n -= 1
			return (key, value)
		except KeyError:
			raise KeyError('Key Error: no key-value entry for '+ repr(key))

	def find(self, key):
		""" Return without removing arbitrary (key, value) pair or raise KeyError if key not in multimap """
		try:
			secondary = self._map[key]
			return (key, secondary[0])
		except KeyError:
			raise KeyError('Key Error: no key-value entry for '+ repr(key))

	def find_all(self, key):
		""" Generate iteration of all (key, value) pairs associated with the key """
		try:
			secondary = self._map[key]
			for value in secondary:
				yield (key, value)
		except KeyError:
			raise KeyError('Key Error: no key-value entry for '+ repr(key))


class TestMultiMap(unittest.TestCase):

	def test_map_empty_when_created(self):
		mm = MultiMap()
		self.assertEqual(len(mm), 0)

	def test_add_values(self):
		mm = MultiMap()
		mm.add('ones', 1)
		mm.add('ones', 2)
		mm.add('ones', 3)
		mm.add('ones', 5)
		mm.add('ones', 5)
		self.assertEqual(len(mm), 5)

	def test_pop(self):
		mm = MultiMap()
		mm.add('ones', 1)
		mm.add('ones', 2)
		mm.add('ones', 3)
		mm.add('ones', 5)
		mm.add('ones', 5)
		self.assertEqual(mm.pop('ones'), ('ones', 5))
		self.assertEqual(len(mm), 4)

	def test_find(self):
		mm = MultiMap()
		mm.add('ones', 1)
		mm.add('ones', 2)
		mm.add('tens', 10)
		mm.add('tens', 20)
		self.assertEqual(mm.find('tens'), ('tens', 10))
		with self.assertRaisesRegex( KeyError, "Key Error: no key-value entry for 'twenties'"):
			mm.find('twenties')

	def test_find_all(self):
		mm = MultiMap()
		mm.add('ones', 1)
		mm.add('ones', 2)
		mm.add('tens', 10)
		mm.add('tens', 20)
		self.assertEqual( list(mm.find_all('tens')), [('tens', 10), ('tens', 20)])

	def test_iterate_over_multimap(self):
		mm = MultiMap()
		mm.add('ones', 1)
		mm.add('ones', 2)
		mm.add('tens', 10)
		mm.add('tens', 20)
		self.assertEqual(set(iter(mm)), {('ones', 1),('ones', 2),('tens', 10),('tens', 20)})


if __name__ == '__main__':
	unittest.main()
