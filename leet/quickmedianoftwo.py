import unittest
import random


class Solution:
	""" 4. Median of Two Sorted Arrays using quickselect: runs in O(n) time """

	def quickSelect(self, arr, k):
		""" selects the k smallest element in an Array arr """
		if len(arr) == 1:
			return arr[0]
		pivot = random.choice(arr)

		L = [x for x in arr if x < pivot]
		E = [x for x in arr if x == pivot]
		G = [x for x in arr if x > pivot]

		if k <= len(L):
			return self.quickSelect(L, k)
		elif k <= len(L) + len(E):
			return pivot
		else:
			j = k - ( len(L) + len(E) )
			return self.quickSelect(G, j)

	def findMedianOfSortedArrays(self, arr1, arr2):
		""" determines the median of two sorted arrays """
		if not isinstance(arr1 or arr2, list):
			raise Exception("Invalid input")
		elif not arr1 and not arr2:
			return
		else:
			joined = arr1+arr2 # O(n+m)
			n = len(joined) # sub one for zero indexing

			if n%2 == 0:
				return ( self.quickSelect(joined, n//2) + self.quickSelect(joined, n//2 + 1 ) ) / 2
			else:
				return self.quickSelect(joined, n//2 + 1)


class TestMedianofTwo(unittest.TestCase):
	soln = Solution()
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.findMedianOfSortedArrays("", "")

	def test_empty_inputs(self):
		self.assertEqual(self.soln.findMedianOfSortedArrays([], []), None)

	def test_rightmedian(self):
		self.assertEqual(self.soln.findMedianOfSortedArrays([1,2], [3,4]), 2.5)

if __name__ == '__main__':
	unittest.main()
