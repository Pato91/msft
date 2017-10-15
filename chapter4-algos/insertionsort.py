import unittest

def insertionSort(arr):
	''' implements the insertion sort on an array
	returns an incrementally sorted array

	Runtime: O(n^2) > worst case, and 0(n) > best case
	'''
	# insertion sort
	n = len(arr)
	for i in range(n):
		j=i
		curr = arr[i]

		while j > 0  and arr[j-1] > curr:
			arr[j] = arr[j-1]
			j -= 1
		arr[j] = curr

	return arr


class TestSort(unittest.TestCase):
	def test_null_case(self):
		self.assertEqual(insertionSort([]), [])

	def test_already_sorted(self):
		self.assertEqual(insertionSort([7, 9, 11, 22, 42, 88, 99]), [7, 9, 11, 22, 42, 88, 99])

	def test_sort(self):
		self.assertEqual(insertionSort([22, 11, 99, 88, 9, 7, 42]), [7, 9, 11, 22, 42, 88, 99])

if __name__ == '__main__':
	unittest.main()
