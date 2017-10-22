import unittest

def unique(lst):
	''' checks if all the elements in lst are unique
	Runtime: O(n^2)
	'''
	n = len(lst)
	for i in range(n):
		for j in range(i+1, n):
			if lst[i] == lst[j]:
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
