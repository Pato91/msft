import random


def quickSelect(arr, k):
	""" Return the kth smallest element of Array arr, for k from 1 to len(arr) """
	n = len(arr)
	if n < k:
		raise Exception('k out of range of sequence')
	if n == 1:
		return arr[0]

	pivot = random.choice(arr)
	L = [x for x in arr if x < pivot]
	E = [x for x in arr if x == pivot]
	G = [x for x in arr if x > pivot]

	if k <= len(L):
		return quickSelect(L, k)
	elif k <=  len(L) + len(E):
		return pivot
	else:
		j = k - len(L) - len(E)
		return quickSelect(G, j)

arr = [3,1,2,7,2,4,3,2,5,8,5,9,2,2,5,2]

print(sorted(arr), len(arr))

print(quickSelect(arr, 9))