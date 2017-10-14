import unittest
from progression import Progression
class ArithmeticProgression(Progression):
	"""Iterator producing an ArithmeticProgression"""
	def __init__(self, start=0, step=1):
		''' Create a new Arithmetic Progression
		start: First term of the progression: default is 0
		step: Constant increment factor of the progression
		'''
		super().__init__(start) #initialize base class
		self._step = step

	def _advance(self):
		''' Update current value by adding the fixed increment '''
		self._current += self._step

	def get_element(self, n):
		''' return nth element of progression '''
		return self._start + (n-1)*self._step


class TestArithmetic(unittest.TestCase):
	def test_create_progression(self):
		self.assertTrue(ArithmeticProgression())

	def test_start_of_progression(self):
		ap = ArithmeticProgression(10)
		self.assertEqual( next(ap), 10)

	def test_progress_by_steps(self):
		ap = ArithmeticProgression(0, 4)
		self.assertEqual( next(ap), 0)
		self.assertEqual( next(ap), 4)
		self.assertEqual( next(ap), 8)

	def test_sum(self):
		ap = ArithmeticProgression(step=2)
		self.assertEqual(ap._sum(5), 20)

	def test_get_nth_value(self):
		ap = ArithmeticProgression(start=0, step=2)
		self.assertEqual(ap.get_element(5), 8)


if __name__ == '__main__':
	unittest.main()
