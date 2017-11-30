def selection(arr):
	""" perform a selection sort on arr, ascending order """
	n = len(arr)
	for i in range(n-1):
		index = i
		least = arr[index]
		for j in range(index, n):
			if arr[j] < least:
				least = arr[j]
				index = j
		arr[i], arr[index] = arr[index], arr[i]
	return arr

arr = [3, 6, 1, 8, 4, 5]

print(selection(arr))
