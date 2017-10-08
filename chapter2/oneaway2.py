import unittest

def oneAway(pair):
	''' returns one away truthy '''
	def oneReplaceAway():
		difference = 0
		for i in range(len1):
			if first[i] != second[i]:
				difference += 1
			if difference > 1:
				return False
		return True

	def oneInsertAway():
		difference = 0
		for i in range(len1):
			if first[i] not in second:
				difference += 1
			if difference > 1:
				return False
		return True

	def oneRemoveAway():
		difference = 0
		for i in range(len2):
			if second[i] not in first:
				difference += 1
			if difference > 1:
				return False
		return True

	if not isinstance(pair, list) or len(pair) != 2 or any(not isinstance(word, str) for word in pair):
		raise Exception('Invalid Input')
	else:
		first = pair[0]
		second = pair[1]

		len1 = len(first)
		len2 = len(second)

		if first == second:
			return True
		elif len1 == len2:
			return oneReplaceAway()
		elif len1 + 1 == len2:
			return oneInsertAway()
		elif len1 - 1 == len2:
			return oneRemoveAway()
		else:
			return False

class Tests(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			oneAway(1)

	def test_equal_length(self):
		self.assertFalse(oneAway(['bulk', 'pulp']))
		self.assertTrue(oneAway(['bulk', 'bulk']))
		self.assertTrue(oneAway(['bulk', 'bulb']))

	def test_empty_strings(self):
		self.assertTrue(oneAway(['b','']))
		self.assertTrue(oneAway(['','']))

	def test_one_away(self):
		self.assertTrue(oneAway(['self', 'selfi']))

	def test_two_away(self):
		self.assertFalse(oneAway(['self', 'selfie']))

if __name__ == '__main__':
unittest.main()
