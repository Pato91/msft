def goodfib(n):
	''' compute the nth fibonacci number
	returns tuple of F(n) and F(n-1)
	Runtime O(n)
	'''
	if n <= 1:
		return n,0
	else:
		(a,b) = goodfib(n-1)
		return a+b, a

print(goodfib(10))
