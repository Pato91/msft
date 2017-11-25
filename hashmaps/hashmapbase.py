from mapbase import MapBase
from random import randrange


class HashMapBase(MapBase):
	"""
	Abstract base class for  map using a hash-table with MAD compression
	@abstract Methods implemented by subclasses:
		_bucket_getitem() , _bucket_setitem() and _bucket_delitem()
	"""
	__slots__ = '_table', '_n', '_prime', '_scale', '_shift' # streamline memory

	def __init__(self, cap = 11, p=109345121):
		""" Create an empty hash-table map """
		self._table = [None]*cap
		self._n = 0 # number of entries in map
		self._prime = p # prime # fro MAD compression
		self._scale = 1 + randrange(p-1) # scale from 1 to p-1 for MAD
		self._shift = randrange(p) # shift from 0 to p-1 for MAD


	def _hash_function(self, key):
		""" Create a MAD compressed hash-code of the key """
		return (hash(key)*self._scale + self._shift) % self._prime %  len(self._table)

	def _resize(self, c):
		""" Resize bucket array to capacity c """
		old = list(self.items()) # record all existing elements
		self._table = [None]*c
		self._n = 0 # will be recomputed in adds below
		for (key, value) in old:
			self[key] = value

	def __len__(self):
		""" Return the number of items in map """
		return self._n

	def __getitem__(self, key):
		""" Get an item associated with key """
		j = self._hash_function(key)
		return self._bucket_getitem(j, key) # may raise key error if key not in map

	def __setitem__(self, key, value):
		""" Store a new key-value pair in map, replace value if key already in map """
		j = self._hash_function(key)
		self._bucket_setitem(j, key, value) # subroutine maintains self._n
		if self._n > len(self._table) // 2: # maintain load factor <= 0.5
			self._resize(2 * len(self._table) - 1)

	def __delitem__(self, key):
		""" Remove a key-value from map """
		j = self._hash_function(key)
		self._bucket_delitem(j, key) # may raise key error if key not in map
		self._n -= 1
