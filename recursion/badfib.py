
def badfib(n):
	''' a very bad fibonacci generator.
	runtime is exponential in n, O(2^n)
	'''
	if n <= 1:
		return 1
	else:
		return badfib(n-2) + badfib(n-1)

print(badfib(9))
