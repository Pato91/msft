def linearsum(lst, n):
	''' Example of linear recursion
	get the sum of a list of integers by recursion
	Runtime: O(n)
	'''
	if n == 0 :
		return 0
	else:
		return lst[n-1] + linearsum(lst, n-1)

print(linearsum([1,2,3,4], 4))
