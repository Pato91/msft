# def bubble(arr):
# 	""" sort a given array in ascending order: bubble sort technique """
# 	n = len(arr) - 1
# 	while n > 1:
# 		for i in range(n):
# 			if arr[i] > arr[i+1]:
# 				arr[i], arr[i+1] = arr[i+1], arr[i]
# 		n -= 1
# 	return arr

def bubble(arr):
	"""
	Sort a given array in ascending order: bubble sort technique
	Uses a flag to stop iterations
	"""
	flag = False
	n = len(arr) - 1
	while n > 1:
		for i in range(n):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				flag = True
		if not flag:
			break
		n -= 1
	return arr

arr = [5, 1, 6, 2, 4, 3]

print(bubble(arr))