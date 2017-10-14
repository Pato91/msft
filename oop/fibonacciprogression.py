import unittest
from progression import Progression
import math

class FibonacciProgression(Progression):
	""" Iterator producing an arithmetic progression """
	def __init__(self, first=0, second=1):
		''' Create a new Geometric Progressions '''
		super().__init__(second)
		self._prev = first

	def _advance(self):
		''' Update current value, multiply by factor '''
		self._prev, self._current = self._current, self._prev + self._current

	def get_element(self, n):
		''' get nth element of progression
		caveat: formula below assumes first = 0, second = 1 '''
		phi = 1.6180339887
		return math.ceil( ( pow(phi, n) - pow( (-phi), (-n)) ) / math.sqrt(5) )


class TestGeometric(unittest.TestCase):
	def test_create_progression(self):
		self.assertTrue(FibonacciProgression())

	def test_progression(self):
		gp = FibonacciProgression()
		self.assertEqual( next(gp), 1)
		self.assertEqual( next(gp), 1)
		self.assertEqual( next(gp), 2)
		self.assertEqual( next(gp), 3)

	def test_sum(self):
		gp = FibonacciProgression(first=1, second=1)
		self.assertEqual(gp._sum(3), 6)

	def test_get_nth_value(self):
		ap = FibonacciProgression(first=1, second=2)
		self.assertEqual(ap.get_element(3), 2)

if __name__ == '__main__':
	unittest.main()
