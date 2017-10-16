import unittest
''' given a string 1a2g3b return aggbbb

    sample test cases can be exteded to handle more cases
'''

def decompress(string):
    ''' returns an expanded string from a compressed input '''
    if not isinstance(string, str) or len(string) < 1 or all( x.isdigit() for x in string ):
        raise Exception('invalid input')
    elif all( x.isalpha() for x in string ): #all are alpha characters, not compressed
        return string
    else:
        num = 0
        result = [] # holder array for decompressed
        for i in string:
            if i.isdigit():
                num = num*10 + int(i) # parse to number
            else:
                result.append( i*num )
                num = 0

        return ''.join(result)


class Test(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaisesRegex(Exception, 'invalid input'):
            decompress([])

    def test_uncompressed(self):
        self.assertEqual(decompress('abcd'), 'abcd')

    def test_compressed(self):
        self.assertEqual(decompress('1a2g3b'), 'aggbbb')
        self.assertEqual(decompress('10a2g3b'), 'aaaaaaaaaaggbbb')

if __name__ == '__main__':
    unittest.main()
