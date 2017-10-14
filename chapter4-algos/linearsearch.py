import unittest

def linearSearch(number):
	''' checks if number is an element of primes:
	if found in primes, then it is a prime number, return True
	if not found, then it is not a prime number, return False
	primes: first 25 prime numbers

	Runtime: linear O(n) > worst case'''
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

	for prime in primes:
		if prime == number:
			return True
	return False


class TestSearch(unittest.TestCase):
	def test_known_prime(self):
		self.assertTrue(linearSearch(67))

	def test_non_prime(self):
		self.assertFalse(linearSearch(30))

	# add test for validating input

if __name__ == '__main__':
	unittest.main()