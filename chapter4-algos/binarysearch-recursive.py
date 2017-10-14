import unittest

def binarySearch(arr, p, l, n):
	''' checks if p is an element of array arr:
	if found in primes, then it is a prime number, return True
	if not found, then it is not a prime number, return False
	p: number to be searched
	l: lower index
	n: length of array segment to be searched

	Runtime: O(log(n)) > logarithmic
	'''
	while l <= n:
		guess = l + (n-l)//2
		if arr[guess] == p:
			return guess
		elif arr[guess] < p:
			l = guess+1
			binarySearch(arr, p, l, n)
		else:
			n = guess-1
			binarySearch(arr, p, l, n)
	return -1

class TestSearch(unittest.TestCase):
	def test_known_prime(self):
		primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
		self.assertEqual(binarySearch(primes, 67, 0, 25), 18)

	def test_non_prime(self):
		primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
		self.assertEqual(binarySearch(primes, 30, 0, 25), -1)

	# add test for validating input

if __name__ == '__main__':
	unittest.main()
