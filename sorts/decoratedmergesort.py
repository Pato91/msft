import unittest
from merge import mergeSort

def decoratedMergeSort(data, key=None):
	"""
	Demonstrate the decorate-sort-undecorate pattern when using a key parameter
	Applies private _Item class to represent key-value pairs
	"""
	class _Item:
		""" Private representation of key-value pair as items """
		__slots__ = '_key', '_value' #steamline memory

		def __init__(self, key, value):
			""" create a new item """
			self._key = key
			self._value = value

		def __lt__(self, other):
			""" Comparison test on items """
			return self._key < other._key

	if key is not None:
		for j in range(len(data)):
			data[j] = _Item(key(data[j]), data[j])

	data = mergeSort(data)

	if key is not None:
		for j in range(len(data)):
			data[j] = data[j]._value

	return data

class TestDecoratedSort(unittest.TestCase):

	def test_sort_without_key(self):
		self.assertNotEqual(['red', 'green', 'blue', 'cyan'], ['blue', 'cyan', 'green', 'red'] )
		self.assertEqual( decoratedMergeSort(['red', 'green', 'blue', 'cyan']), ['blue', 'cyan', 'green', 'red'] )

	def test_sort_with_key(self):
		self.assertNotEqual(['red', 'green', 'blue', 'cyan'], ['blue', 'cyan', 'green', 'red'])
		self.assertEqual( decoratedMergeSort(['red', 'green', 'blue', 'cyan'], key=len), ['red', 'cyan', 'blue', 'green'])

if __name__ == '__main__':
	unittest.main()
