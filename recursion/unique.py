import unittest

def unique(lst):
	''' checks if all the elements in lst are unique
	Worst case runtime: O(nlogn) while sorting:
	Comparison is O(n) - linear time
	'''
	n = len(lst)
	temp = sorted(lst)
	for i in range(	1, n):
		if temp[i-1] == temp[i]:
			return False
	return True


class Test(unittest.TestCase):
	def test_invalid_input(self):
		pass

	def test_unique(self):
		self.assertTrue(unique([1,2,3,4,5]))

	def test_repeated(self):
		self.assertFalse(unique([1,2,3,4,1]))


if __name__ == '__main__':
	unittest.main()
