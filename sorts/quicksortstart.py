def quickSort(arr, start, end):
	""" quicksort with pivot always at the start """
	def _partition(arr, start, end):
		pivot = arr[start]
		i = end+1 # track index of pivot after partitioning
		for j in range(end, start, -1):
			if arr[j] >= pivot:
				i-=1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i-1], arr[start] = pivot, arr[i-1]
		return i-1

	if start < end:
		p = _partition(arr, start, end)

		quickSort(arr, start, p-1)
		quickSort(arr, p+1, end)

	return arr

arr = [10, 3, 100, 20, 33, 70, 0]

print(quickSort(arr, 0, 6))
