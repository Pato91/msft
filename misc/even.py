import unittest

def is_even(n):
	''' check for evenness of a number without using modulo, division or multiplication operators

	# equivalent modulo evenness check
	def is_even(n): return n % 2 == 0
	'''
	check = 0
	while True:
		if check == n:
			return True
		elif check > n:
			break
		else:
			check += 2
	return False

class Test(unittest.TestCase):
	def test_even(self):
		self.assertTrue(is_even(2))

	def test_not_even(self):
		self.assertFalse(is_even(3))

if __name__ == '__main__':
	unittest.main()
