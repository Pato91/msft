import unittest

class SequenceIterator(object):
	''' Iterator of any of the Python's sequence types '''
	def __init__(self, sequence):
		super(SequenceIterator, self).__init__()
		''' create an iterator for the given sequence '''
		self._seq = sequence
		self._n = -1 # start from -1, increment to 0 on first call to nexts

	def __next__(self):
		''' return the next element else raise StopIteration error '''
		self._n += 1
		if self._n < len(self._seq):
			return (self._seq[self._n])
		raise StopIteration('End of sequence')

	def __iter__(self):
		''' an iterator must return itself as an iterator '''
		return self


class TestIterator(unittest.TestCase):
	def test_create_iterator(self):
		self.assertTrue(SequenceIterator([]))

	def test_iterator_yields(self):
		seq = [1, 2, 3, 4]
		miter = SequenceIterator(seq)
		self.assertEqual( next(miter), 1)
		self.assertEqual( next(miter), 2)
		self.assertEqual( next(miter), 3)
		self.assertEqual( next(miter), 4)
		with self.assertRaisesRegex(StopIteration, 'End of sequence'):
			next(miter)
		# self.assertTrue( i in seq for i in iter(miter))


if __name__ == '__main__':
	unittest.main()
