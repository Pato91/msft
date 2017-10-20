def factorial(n):
	''' recursively compute the factorial of a number n '''
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)

print(factorial(3))

''' Notes:
base case is 0
each time the function is called with a value reuced by one
stops when base case is reached
'''