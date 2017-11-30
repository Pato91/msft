def merge(arr1, arr2):
	""" merges two sorted arrays arr1 and arr2 """
	m = len(arr1)
	n = len(arr2)
	arr = [None]*(n+m)

	i = j = 0
	while (i + j) < (m + n):
		if j == n or ( i < m and arr1[i] < arr2[j] ):
			arr[i+j] = arr1[i]
			i+=1
		else:
			arr[i+j] = arr2[j]
			j+=1
	return arr

def mergeSort(arr):
	""" Sort an array in ascending order: merge sort """
	n = len(arr)
	if n < 2:
		return arr # already sorted
	mid = n // 2
	arr1 = mergeSort(arr[:mid])
	arr2 = mergeSort(arr[mid:])

	return merge(arr1, arr2)


# arr = [10, 3, 100, 20, 33, 70, 0]

# print(mergeSort(arr))
