
def heapSort(arr):

	def _heapify(n, root):
		largest = root # assume largest is the root of heap subtree
		l = root*2 + 1 # index of left child
		r = root*2 + 2 # index of right child

		if l < n and  arr[l] > arr[largest]: # largest is left child
			largest = l
		if r < n and arr[r] > arr[largest]: # largest is right child
			largest = r

		if largest != root:
			arr[largest], arr[root] = arr[root], arr[largest]
			_heapify(n, largest) # recursively heapify affected branch

	n = len(arr)

	# build a maxheap
	for i in range(n, -1, -1):
		_heapify(n, i) # this heapifies subtrees first!

	# extract elements from heap
	for i in range(n-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		_heapify(i, 0)
	return arr

arr = [12, 11, 13, 5, 6, 7]
print(heapSort(arr))
