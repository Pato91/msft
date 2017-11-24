import unittest


class PriorityQueueBase:
	""" Abstract base class for priority queue """
	class _Item:
		""" Non-public lightweight composite to store priority queue items """
		__slots__ = '_key', '_value' # streamline memory

		def __init__(self, key, value):
			""" Initialize a key-value pair item object """
			self._key = key
			self._value = value

		def __lt__(self, other):
			""" Compare items based on their keys """
			return self._key < other._key

	def is_empty(self):
		""" Return True if prioroty queue is empty """
		return len(self) == 0


class TestPQueueBase(unittest.TestCase):
	def test_something(self):
		pass

if __name__ == '__main__':
	unittest.main()
