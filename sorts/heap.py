
def heapify(heap, n, root):
	"""  balance heap according to order and shape properties """
	smallest = root # parent, assume parent is the smallest in tree
	l = 2*root + 1 # left child
	r = 2*root + 2 # right child

	if l < n and heap[l] < heap[smallest]:
		smallest = l
	if r < n and heap[r] < heap[smallest]:
		smallest = r

	if smallest != root:
		heap[root], heap[smallest] = heap[smallest], heap[root]
		heapify(heap, n, smallest) # recursively heapify affected subtree

def heapSort(arr):
	""" make a heap out of input data """
	n = len(arr)
	for i in range(n, -1, -1):
		heapify(arr, n, i) # heapify the subtrees and then their parent trees

	# extract elements from heap
	for i in range(n-1, 0, -1):
		if arr[i] < arr[i-1]:
			arr[i], arr[i-1] = arr[i-1], arr[i]
			heapify(arr, i, 0)
	return arr

# arr = [4, 10, 3, 5, 1, 13]
arr = [12, 11, 13, 5, 6, 7, 10]

print(heapSort(arr))
