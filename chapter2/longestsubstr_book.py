import unittest

def longestSub(string):
	''' returns the length of longest substring of consecutive unique characters '''

	# validate input
	if not isinstance(string, str) or len(string) == 0:
		raise Exception('Invalid Input')

	max_length = 0

	n = len(string)
	sub = set()   #substring hash set

	# tracking position
	i = j = 0

	while i < n and j < n:
		if string[j] not in sub:
			sub.add(string[j])
			j+=1
			max_length = max( max_length, j-i )
		else:
			sub.remove(string[i])
			i+=1		

	return max_length

# Tests
class Tests(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			longestSub('')

	def test_single_character_input(self):
		self.assertEqual(longestSub('a'), 1)

	def test_mixed_case_input(self):
		self.assertEqual(longestSub('aAbc'), 4)

	def test_single_repeat_character(self):
		self.assertEqual(longestSub('aaaaaaa'), 1)

	def test_two_repeat_characters(self):
		self.assertEqual(longestSub('aaaabbbb'), 2)

	def test_global_no_repeat(self):
		self.assertEqual(longestSub('abcde'), 5)

	def test_known_cases(self):
		self.assertEqual(longestSub('pwwkew'), 3)
		self.assertEqual(longestSub('abcabcbb'), 3)
		self.assertEqual(longestSub('abchdaaaabcda'), 5)

if __name__ == '__main__':
	unittest.main()
