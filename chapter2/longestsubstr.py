import unittest

def longestSub(string):
	''' returns the longest substring of consecutive unique characters '''

	# validate input
	if not isinstance(string, str) or len(string) == 0:
		raise Exception('Invalid Input')

	# generate substrings :> can I use regex for this?
	anchor = current = future = 0 #visualization in TEBOW image of the day
	max_substr = string[anchor]

	sub = string[anchor:future]

	while future < len(string):
		# repeats
		if string[future]  != string[current] and string[future] not in sub:
			current, future = future, future+1
		else:
			anchor = current = future
			future+=1

		sub = string[anchor:future]
		if len(max_substr) < len(sub):
			max_substr = sub

	return max_substr

# Tests
class Tests(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			longestSub('')

	def test_single_character_input(self):
		self.assertEqual(longestSub('a'), 'a')

	def test_mixed_case_input(self):
		self.assertEqual(longestSub('aAbc'), 'aAbc')

	def test_single_repeat_character(self):
		self.assertEqual(longestSub('aaaaaaa'), 'a')

	def test_two_repeat_characters(self):
		self.assertEqual(longestSub('aaaabbbb'), 'ab')

	def test_global_no_repeat(self):
		self.assertEqual(longestSub('abcde'), 'abcde')

	def test_known_cases(self):
		self.assertEqual(longestSub('pwwkew'), 'wke')
		self.assertEqual(longestSub('abcabcbb'), 'abc')
		self.assertEqual(longestSub('abchdaaaabcda'), 'abchd')

if __name__ == '__main__':
	unittest.main()
