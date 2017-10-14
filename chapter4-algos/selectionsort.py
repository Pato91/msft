import unittest

def selectionSort(arr):
	''' implements the selection sort on an array
	returns an incrementally sorted array

	Runtime: Theta(n^2) > quadratic
	'''

	def swap(arr, i, j):
		''' swaps elements at index i and j of an array'''
		arr[i], arr[j] = arr[j], arr[i]
		return arr

	# selection sort
	n = len(arr)
	for i in range(n):
		small = i #index of smallest in sub array
		for j in range(i, n):
			if arr[j] < arr[small]:
				small = j
		arr = swap(arr, i, small)
	return arr


class TestSort(unittest.TestCase):
	def test_null_case(self):
		self.assertEqual(selectionSort([]), [])

	def test_already_sorted(self):
		self.assertEqual(selectionSort([7, 9, 11, 22, 42, 88, 99]), [7, 9, 11, 22, 42, 88, 99])

	def test_sort(self):
		self.assertEqual(selectionSort([22, 11, 99, 88, 9, 7, 42]), [7, 9, 11, 22, 42, 88, 99])

if __name__ == '__main__':
	unittest.main()
