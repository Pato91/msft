def urlify(string):
	""" replace all spaces in string with '%20' """
	return string.replace(' ', '%20')

print(urlify('Jodom is one hell a mofo'))

def urlify(string):
	""" replace all spaces in string with '%20' """
	swap = []
	for c in string:
		swap.append('%20') if c == ' ' else swap.append(c)
	return ''.join(swap)

print(urlify('Jodom is one hell a mofo'))
