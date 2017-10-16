import unittest

def revlist(lst):
    ''' Reverses a list
    Worst runtime, O(n) > runs in O(n/2)
    inplace reverse, space complexity of O(1)
    '''

    # validate input
    if not isinstance(lst, list):
        raise Exception('Invalid Input')
    elif len(lst) < 2:
        return lst
    else:
        i = 0 # left
        j = len(lst) - 1 # right

        while i < j:
            lst[i], lst[j] = lst[j], lst[i] # swap left and right
            i += 1
            j -= 1

        return lst


class Tests(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaisesRegex(Exception, 'Invalid Input'):
            revlist('')

    def test_single_digit_or_lower(self):
        self.assertEqual(revlist([]), [])
        self.assertEqual(revlist([1]), [1])

    def test_reverse_even_length(self):
        self.assertEqual(revlist([1,2,3,4]), [4,3,2,1])

    def test_reverse_odd_length(self):
        self.assertEqual(revlist([1,2,3,4,5]), [5,4,3,2,1])

if __name__ == '__main__':
    unittest.main()
