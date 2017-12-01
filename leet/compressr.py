import unittest

def compress(string):
	""" string compression """
	if not isinstance(string, str) or any(c.isdigit() for c in string):
		raise Exception('Invalid input string')
	else:
		n = len(string)

		if n <= 2:
			return string

		i = j = 0
		count = 1
		cp = []

		while j < n:
			j += 1
			if j < n and string[i] == string[j]:
				count+=1
				continue
			elif j < n:
				cp.extend([string[i], str(count)])
				i, count = j, 1
				continue
			else:
				cp.extend([string[i], str(count)])

		return ''.join(cp) if len(cp) < n else string


class Tests(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaisesRegex(Exception, 'Invalid input string'):
            compress(['abc','aaabddde'])
        with self.assertRaisesRegex(Exception, 'Invalid input string'):
            compress('abc123')

    def test_empty_string(self):
        self.assertEqual(compress('   '), ' 3')

    def test_single_digit_str(self):
        self.assertEqual(compress('s'), 's')

    def test_mixed_case(self):
        self.assertEqual(compress('aaaAAA'), 'a3A3')

    def test_equal_length_case(self):
        self.assertEqual(compress('aaaA'), 'aaaA')

if __name__ == '__main__':
    unittest.main()

