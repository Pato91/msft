import unittest

def bubbleSort(arr):
	''' implements the bubble sort on an array
	returns an incrementally sorted array

	Runtime: O(n^2) > worst case, and 0(n) > best case
	'''
	# bubble sort - recursive
	flag = 0 # track the need for futher recursions
	n = len(arr)
	for i in range(n-1):
		if arr[i] > arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]
		if i >0 and arr[i] < arr[i-1]:
			flag = 1  # further recursion case
	if flag:
		bubbleSort(arr)
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
