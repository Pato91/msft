import random

def quickSelect(arr, k):
	""" Returns the kth smallest element in an Array arr, for k in range 1 to len(arr) """
	while True:
		if len(arr) == 1:
			return arr[0]

		pivot = random.choice(arr) # pick random pivot

		L = [x for x in arr if x < pivot]
		E = [x for x in arr if x == pivot]
		G = [x for x in arr if x > pivot]

		if k <= len(L):
			arr = L
			continue
		elif k <= len(L) + len(E):
			return pivot
		else:
			k-=(len(L) + len(E))
			arr = G
			continue

arr = [3,1,2,7,2,4,3,2,5,8,5,9,2,2,5,2]

print(quickSelect(arr, 9))
