import unittest

def threewaydisjoint(A, B, C):
	''' determines that the intersection between three sets is empty
	no element x such that x is in A, x is in B and x is in C
	Worst runtime, O(n^3) if A, B, C are size n
	'''
	for x in A:
		for y in B:
			for z in C:
				if x == y == z:
					return False, 'sets have common elements'
	return True, 'sets are disjoint'


class TestThreeWayDisjoint(unittest.TestCase):
	def test_invalid_input(self):
		pass

	def test_disjoint(self):
		self.assertTrue(threewaydisjoint([1,2,3,4], [5,6,7,8,9], [11,12,13,14,15])[0])

	def test_joined(self):
		self.assertFalse(threewaydisjoint([1,2,3,4,5], [5,6,7,8,9], [1,5,6,3,8])[0])

if __name__ == '__main__':
	unittest.main()
