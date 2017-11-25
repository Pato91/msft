import unittest
from sortedtablemap import SortedTableMap


class CostPerformanceDB:
	""" Maintain a database of maximal (cost, performance) pairs """

	def __init__(self):
		""" Create an empty database """
		self._DB = SortedTableMap()

	def best(self, budget):
		"""
		Return (cost, performance) pair with largest cost not exceeding budget
		None if no pair exists within budget
		"""
		return self._DB.find_le(budget)

	def add(self, c, p):
		""" Add new entry with cost c and performance p """

		'''' Fluff functionality ----------------

		#determine if (c, p) is dominated by an existing pair
		other = self._DB.find_le(c) # other is at least as cheap as c
		if other is not None and other[1] >= p: # and its performance is at least as good
			return # new (c, p) is dominated so ignore
		'''
		self._DB[c] = p

		'''' More fluff functionality ----------------

		# and then remove any pairs dominate dby (c, p)
		other = self._DB.find_gt(c) # entry more expensive than c
		while other is not None:
			del self._DB[other[0]]
			other = self._DB.find_gt(c)
		'''


class TestCostPerformanceDB(unittest.TestCase):
	def test_create_db(self):
		self.assertTrue(CostPerformanceDB())

if __name__ == '__main__':
	unittest.main()
