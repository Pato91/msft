import unittest
from progression import Progression

class GeometricProgression(Progression):
	""" Iterator producing an arithmetic progression """
	def __init__(self, start=1, factor=2):
		''' Create a new Geometric Progressions '''
		super().__init__(start)
		self._factor = factor

	def _advance(self):
		''' Update current value, multiply by factor '''
		self._current *= self._factor

	def get_element(self, n):
		''' get nth element of progression '''
		return self._start * pow( self._factor, n-1)


class TestGeometric(unittest.TestCase):
	def test_create_progression(self):
		self.assertTrue(GeometricProgression())

	def test_progression(self):
		gp = GeometricProgression()
		self.assertEqual( next(gp), 1)
		self.assertEqual( next(gp), 2)
		self.assertEqual( next(gp), 4)

	def test_sum(self):
		gp = GeometricProgression(factor=2)
		self.assertEqual(gp._sum(3), 7)

	def test_get_nth_value(self):
		ap = GeometricProgression(start=1, factor=2)
		self.assertEqual(ap.get_element(3), 4)

if __name__ == '__main__':
	unittest.main()
