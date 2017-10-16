import unittest

def compress(string):
    ''' compresses a string with repeat characters '''
    if not isinstance(string, str) or len(string) == 0 or any(x.isdigit() for x in string):
        raise Exception('Invalid input string')
    elif( len(string) <= 2 ):
        return string
    else:
        compressed = []
        i = j = 0
        count = 0
        while j < len(string):
            if string[i] == string[j]:
                count+=1
            else:
                compressed.extend( [ string[i], str(count) ] )
                i = j
                count = 1
            j+=1
        compressed.extend( [ string[i], str(count) ] )

        if len(compressed) < len(string):
            return ''.join(compressed)
        return string


class Tests(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaisesRegex(Exception, 'Invalid input string'):
            compress('')
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
