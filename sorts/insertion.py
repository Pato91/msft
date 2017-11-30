def insertion(arr):
	""" sort an array in ascending order: insertion sort """
	for i in range(len(arr)):
		key = arr[i]
		j = i
		while j > 0 and arr[j-1] > key:
			arr[j] = arr[j-1]
			j -= 1
		arr[j] = key
	return arr

arr = [5, 1, 6, 2, 4, 3]

print(insertion(arr))
