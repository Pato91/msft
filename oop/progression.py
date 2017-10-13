import unittest

class Progression(object):
	"""An iterator producing a generic Progression
	default iterator produces 0, 1, 2, 3, ... infinitely"""
	def __init__(self, start=0):
		''' Initialize current to the first value in progression '''
		super(Progression, self).__init__()
		self._current = start

	def _advance(self):
		''' Update current to a new value
		Should be overidden by a subclass to customize progression
		Convention: if current is set to None, thats the end of a finite progression
		'''
		self._current += 1

	def __next__(self):
		''' Return next element in iterator, raise StopIteration otherwise '''
		if self._current is None:
			raise StopIteration()
		else:
			answer = self._current
			self._advance()
			return answer

	def __iter__(self):
		''' an iterator must return itself: convention '''
		return self

	def print_progression(self, n):
		''' prints next n values of progression '''
		return ' '.join( str( next(self)) for i in range(n) )


class TestProgression(unittest.TestCase):
	def test_create_progression(self):
		self.assertTrue(Progression())

	def test_progress_to_new_value(self):
		p = Progression()
		p._advance()
		self.assertEqual(p._current, 1)

	def test_next_value_iteration(self):
		p = Progression()
		self.assertEqual(next(p), 0)
		self.assertEqual(next(p), 1)

	def test_print_progression_in_range(self):
		p = Progression()
		self.assertEqual(p.print_progression(6), '0 1 2 3 4 5')


if __name__ == '__main__':
	unittest.main()
