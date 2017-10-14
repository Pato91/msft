import unittest

def binarySearch(number):
	''' checks if number is an element of primes:
	if found in primes, then it is a prime number, return True
	if not found, then it is not a prime number, return False
	primes: first 25 prime numbers

	Runtime: O(log(n)) > logarithmic
	'''
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

	lower = 0
	upper = len(primes)-1

	while True:
		guess = (lower + upper) // 2

		if upper < lower:
			return False
		elif number == primes[guess]:
			return True
		elif number > primes[guess]:
			lower = guess+1
		else:
			upper = guess-1


class TestSearch(unittest.TestCase):
	def test_known_prime(self):
		self.assertTrue(binarySearch(67))

	def test_non_prime(self):
		self.assertFalse(binarySearch(30))

	# add test for validating input

if __name__ == '__main__':
	unittest.main()