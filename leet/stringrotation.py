def isSubstring(s1, s2):
	""" checks if s1 is a substring of s2 """
	return s2.find(s1) != -1

def isRotation(first, second):
	"""
	Check if the second is a rotation of the first
	Use only a single call to isSubstring
	example:
		isRotation('erbottlewat', 'waterbottle') >> True
	"""

	if not isinstance(first or second, str) or len(first) != len(second):
		raise Exception('Invalid input')
	elif first == second:
		return False
	else:
		return isSubstring(second, first*2)


print( isSubstring('joe', 'joedom'))
print( isRotation('domjoe', 'joedom'))
print( isRotation('domjoe', 'domjom'))
print( isRotation('domjoe', 'domjoe'))