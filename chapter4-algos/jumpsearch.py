import unittest
import math

def jumpsearch(arr, p):
	''' looks for p in array m:
	return the index of p, otherwise returns -1 if not found

	Runtime: O(root(n)) > worst case
	'''
	n = len(arr)
	m = int( math.sqrt(n) ) # best interval for jumps root(n)

	for i in range(0, n, m):
		if arr[i] == p:
			return i
		elif arr[i] > p:
			for j in range(i-m+1, i): # range for linear search
				if arr[j] == p:
					return j

	return -1


class TestJump(unittest.TestCase):
	def test_found(self):
		arr = [1, 2, 3, 4, 5, 6, 7, 8]
		self.assertEqual(jumpsearch(arr, 3), 2)

	def test_not_found(self):
		arr = [1, 2, 3, 4, 5, 6, 7, 8]
		self.assertEqual(jumpsearch(arr, 9), -1)

if __name__ == '__main__':
	unittest.main()
