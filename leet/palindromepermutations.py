def counter(string):
	""" generates a hashmap of occurences of characters in string """
	count = dict()
	for c in string:
		count[c] = count.get(c, 0) + 1
	return count

def checker(string):
	""" checks if a string is a permutation of a palindrome """
	string = string.lower().replace(' ', '')
	count = counter(string)

	odds = 0 # number of uneven characters in string

	for value in count.values():
		if value % 2 != 0:
			odds += 1
		if odds > 1:
			return False
	return True

print(checker('Tact Coa'))
print(checker('Tact Coaa'))
