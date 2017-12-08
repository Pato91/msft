def atoi(string):
	""" converts a string to integer """
	n = len(string)
	number = 0

	for p in range(n):
		c = string[n-(p+1)]
		if not c.isdigit():
			raise ValueError('Alpha is not digit')
		number += int(c) * (10**p)
	return number

print(atoi('123'))
print(atoi('10002313214'))