import math
""" Merge an array data structure withour recursion """

def merge(src, result, start, inc):
	""" Merge arc[start:start+inc] and src[start+inc:start+2*inc] into result """
	end1 = start+inc
	end2 = min(start+2*inc, len(src))

	x,y,z = start, start+inc, start
	while x < end1 and y < end2:
		if src[x] < src[y]:
			result[z] = src[x]
			x += 1
		else:
			result[z] = src[y]
			y += 1
		z += 1
	if x < end1:
		result[z:end2] = src[x:end1]
	elif y < end2:
		result[z:end2] = src[y:end2]

def mergeSort(arr):
	""" Sort the elements of arr using the merge-sort algorithm """
	n = len(arr)
	logn = math.ceil(math.log(n, 2))
	src, dest = arr, [None]*n

	for i in (2**k for k in range(logn)):
		for j in range(0, n, 2*i):
			merge(src, dest, j, i)
		src, dest = dest, src
	if arr is not src:
		arr[0:n] = src[0:n]
	return arr


arr = [10, 3, 100, 20, 33, 70, 0]

print(mergeSort(arr))
