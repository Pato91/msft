import unittest

def mergeSort(arr, start, end):
	''' implements the merge sort on an array
	returns an incrementally sorted array

	Runtime: O(n^2) > worst case, and 0(n) > best case
	'''
	def merge(arr, start, middle, end):
		''' merge arrays together '''
		n1 = middle-start + 1
		n2 = end-middle

		# temporary arrays
		left = [0]*n1
		right = [0]*n2

		# copy data to temporary arrays
		for i in range(n1):
			left[i] = arr[ start+i ]
		for j in range(n2):
			right[j] = arr[ middle+1+j ]

		# merge temporaries back into arr[start, end]
		i, j = 0, 0
		k = start
		while i < n1 and j < n2:
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		#copy remaining elements of left[] array if any
		while i < n1:
			arr[k] = left[i]
			i += 1
			k += 1

		#copy remaining elements of right[] array if any
		while j < n2:
			arr[k] = right[j]
			j += 1
			k += 1
		return arr

	# merge sort - recursive
	if start < end:
		middle = ( start + (end-1) )//2
		mergeSort(arr, start, middle)
		mergeSort(arr, middle+1, end)
		merge(arr, start, middle, end)

	return arr


class TestSort(unittest.TestCase):
	def test_null_case(self):
		self.assertEqual(mergeSort([], 0, 0), [])

	def test_already_sorted(self):
		self.assertEqual(mergeSort([7, 9, 11, 22, 42, 88, 99], 0, 6), [7, 9, 11, 22, 42, 88, 99])

	def test_sort(self):
		self.assertEqual(mergeSort([22, 11, 99, 88, 9, 7, 42], 0, 6), [7, 9, 11, 22, 42, 88, 99])

if __name__ == '__main__':
	unittest.main()
