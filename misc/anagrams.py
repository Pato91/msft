import unittest

def anagramChecker(first, second):
    ''' checks if first word and second words are anagrams '''
    if not isinstance(first, str) or not isinstance(second, str) :
        raise Exception('invalid input')
    elif first == second:
        return True
    elif len(first) == len(second):
        if set(first) == set(second):
            return True
    return False

class Test(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaisesRegexp(Exception, 'invalid input'):
            anagramChecker('wprd', [])

    def test_not_anagrams(self):
        self.assertFalse(anagramChecker('word', 'food'))

    def test_anagrams(self):
        self.assertTrue(anagramChecker('sword', 'words'))

if __name__ == '__main__':
    unittest.main()
