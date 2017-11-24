from collections import MutableMapping


class MapBase(MutableMapping):
	""" An abstract base class to extend the mutable map ADT """
	class _Item:
		""" Lightweight composite to store key-value pairs as map items """
		__slots__ = '_key', '_value'
		def __init__(self, key, value):
			""" Instantiate a new Item store """
			self._key = key
			self._value = value

		def __eq__(self, other):
			""" Compare items based on thei keys """
			return self._key == other._key

		def __ne__(self, other):
			""" opposite of __eq__ """
			return not (self == other)

		def __lt__(self, other):
			""" Less-than comparator based on keys """
			return self._key < other._key
