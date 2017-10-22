import unittest

def twowaydisjoint(A, B):
	''' determines that the intersection between two sets is empty
	no element x such that x is in A and x is in B
	worst runtime, O(n)
	'''
	for x in A:
		if x in B:
			return False, 'sets have common elements'
	return True, 'sets are disjoint'

class TestTwoWayDisjoint(unittest.TestCase):
	def test_invalid_input(self):
		pass

	def test_disjoint(self):
		self.assertTrue(twowaydisjoint([1,2,3,4], [5,6,7,8,9])[0])

	def test_joined(self):
		self.assertFalse(twowaydisjoint([1,2,3,4,5], [5,6,7,8,9])[0])

if __name__ == '__main__':
	unittest.main()
