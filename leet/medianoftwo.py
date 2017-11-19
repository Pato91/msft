import unittest


class Solution:
	""" 4. Median of Two Sorted Arrays """
	def findMedianOfSortedArrays(self, arr1, arr2):
		""" determines the median of two sorted arrays """
		if not isinstance(arr1 or arr2, list):
			raise Exception("Invalid input")
		elif not arr1 and not arr2:
			return
		else:
			joined = arr1+arr2 # O(n+m)
			joined.sort()  # implement a sort?

			print(joined)

			n = len(joined) - 1 # sub one for zero indexing

			if n%2 == 0:
				return joined[n//2]
			else:
				return ( joined[n//2] + joined[ n//2 +1 ] ) / 2


class TestMedian(unittest.TestCase):
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
