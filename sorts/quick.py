def quickSort(arr, low, high):
	"""
	Sort arr in an ascendign order
	low: first index in the array
	high: last index in the array
	"""
	def partition(arr, low, high):
		""" partition the array into two, with
		pivot at a central location,
		elements left of pivot are less than it
		elements right of pivot are greater than it
		"""
		pivot = arr[high] # last index based pivot
		i = low-1 # start at a negative, index of last smaller element
		for j in range(low, high):
			if arr[j] <= pivot:
				i+=1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i+1], arr[high] = arr[high], arr[i+1]
		return i+1

	if low < high:
		 p =partition(arr, low, high) # position of pivot after partitioning

		 quickSort(arr, low, p-1)
		 quickSort(arr, p+1, high)

	return arr

arr = [10, 3, 100, 20, 33, 70, 0]

print(quickSort(arr, 0, 6))
