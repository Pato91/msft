import unittest

def encode(string, num_shift, char_shift):
	''' returns an encoded string '''
	encoded = []
	for c in string:
		value = ord(c)

		# numbers
		min_number = ord('0')
		max_number = ord('9')
		if value in range(min_number, max_number+1):
			value += num_shift
			if value > max_number:
				value = value%max_number + min_number;
			elif value < min_number:
				value = max_number+1 - (min_number-value);
			encoded.append(chr(value))
			continue

		# lowercase letters
		min_lower = ord('a')
		max_lower = ord('z')
		if value in range(min_lower, max_lower+1):
			value += char_shift
			if value > max_lower:
				value = value%max_lower + min_lower-1;
			elif value < min_lower:
				value = max_lower+1 - (min_lower-value);
			encoded.append(chr(value))
			continue

		# uppercase letters
		min_upper = ord('A')
		max_upper = ord('Z')
		if value in range(min_upper, max_upper+1):
			value += char_shift
			if value > max_upper:
				value = value%max_upper + min_upper-1;
			elif value < min_upper:
				value = max_upper+1 - (min_upper-value);
			encoded.append(chr(value))
			continue

		# special characters
		encoded.append(c)

	return ''.join(encoded)

def caesarShift(string):
	''' encodes a tring using caesars cipher '''
	if len(string) <= 0 or not ':' in string or string.index(':') == 0 or len(string[string.index(':'):])<=1:
		raise Exception('invalid input')
	else:
		shift = int(string[:string.index(':')])
		shift_string = string[string.index(':')+1 :]

		if shift == 0:
			return shift_string

		elif shift<0:
			num_shift = -1*(abs(shift) % 9)
			char_shift = -1*(abs(shift) % 26)
			return encode(shift_string, num_shift, char_shift)
		else:
			num_shift = shift % 9
			char_shift = shift % 26
			return encode(shift_string, num_shift, char_shift)


class Tests(unittest.TestCase):
	def test_something(self):
		pass

	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'invalid input'):
			caesarShift('') #empty input
		with self.assertRaisesRegex(Exception, 'invalid input'):
			caesarShift(':abcd') #no shift value
		with self.assertRaisesRegex(Exception, 'invalid input'):
			caesarShift('abcd') #no shift value
		with self.assertRaisesRegex(Exception, 'invalid input'):
			caesarShift('3:') #no string to encode

	def test_encode_lowercase(self):
		self.assertEqual(encode('some text', 1, 1), 'tpnf ufyu')

	def test_encode_uppercase(self):
		self.assertEqual(encode('SOME TEXT', 1, 1), 'TPNF UFYU')

	def test_encode_numbers(self):
		self.assertEqual(encode('1234', 1, 1), '2345')

	def test_encode_special_chars(self):
		self.assertEqual(encode(' &#$%', 1, 1), ' &#$%')

	def test_zero_shift(self):
		self.assertEqual(caesarShift('0:abcd9'), 'abcd9')

	def test_negative_shift(self):
		self.assertEqual(caesarShift('-1:9'), '8')
		self.assertEqual(caesarShift('-10:9'),'8')
		self.assertEqual(caesarShift('-1:abcd'), 'zabc')
		self.assertEqual(caesarShift('-27:abcd'), 'zabc')

	def test_num_shift(self):
		self.assertEqual(caesarShift('10:1'), '2')

	def test_char_shift(self):
		self.assertEqual(caesarShift('27:z'), 'a')

	def test_mixed_case(self):
		self.assertEqual(caesarShift('27:zZbB* '), 'aAcC* ')

	def test_edge_case(self):
		self.assertEqual(caesarShift('-10000000:zZbB* '), caesarShift('-10:zZbB* '))


if __name__ == '__main__':
	unittest.main()
