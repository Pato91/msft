import unittest

class Range(object):
	""" Model for the python range() function """
	def __init__(self, start, stop = None, step = 1):
		''' initialize a Range instance
		semantics similar to built-in range class '''
		super(Range, self).__init__()

		if stop == None:
			self._start, self._stop = 0, start
		else:
			self._start, self._stop = start, stop

		if step == 0:
			raise ValueError('step cannot be zero')
		else:
			self._step = step

		# calculate and store length attribute
		self._length = max(0, (self._stop - self._start + self._step -1) // self._step )

	def __len__(self):
		''' return number of entries in range '''
		return self._length

	def __getitem__(self, index):
		''' return range element at the index provided '''
		if index < 0:
			index += len(self)
		if not 0 <= index < self._length:
			raise IndexError('index out of range')
		return self._start + index * self._step

		
class TestRange(unittest.TestCase):

	def test_no_stop_provided(self):
		r = Range(2)
		self.assertEqual(r._start, 0)
		self.assertEqual(r._stop, 2)

	def test_default_step(self):
		r = Range(2)
		self.assertEqual(r._step, 1)

	def test_zero_step(self):
		with self.assertRaisesRegex(ValueError, 'step cannot be zero'):
			Range(1, 3, 0)

	def test_create_range(self):
		self.assertTrue(Range(0, 5, 2))

	def test_length(self):
		r = Range(2)
		self.assertEqual(len(r), 2)

	def test_get_item_in_range(self):
		r = Range(3)
		self.assertEqual(r[2], 2)

	def test_iter_on_range(self):
		r = iter(Range(3))
		self.assertEqual(next(r), 0)
		self.assertEqual(next(r), 1)
		self.assertEqual(next(r), 2)
		with self.assertRaises(StopIteration):
			next(r)


if __name__ == '__main__':
	unittest.main()
