import unittest

def bubbleSort(arr):
	''' implements the bubble sort on an array
	returns an incrementally sorted array

	Runtime: O(n^2) > worst case, and 0(n) > best case
	'''
	# bubble sort - recursive
	n = len(arr)
	for i in range(n):
		flag = 1 # track the need for futher iterations
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				flag = 0  # further iteration
		if flag:
			break
	return arr


class TestSort(unittest.TestCase):
	def test_null_case(self):
		self.assertEqual(bubbleSort([]), [])

	def test_already_sorted(self):
		self.assertEqual(bubbleSort([7, 9, 11, 22, 42, 88, 99]), [7, 9, 11, 22, 42, 88, 99])

	def test_sort(self):
		self.assertEqual(bubbleSort([22, 11, 99, 88, 9, 7, 42]), [7, 9, 11, 22, 42, 88, 99])

if __name__ == '__main__':
	unittest.main()
