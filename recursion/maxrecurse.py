import unittest

def maximum(lst, start, stop):
    ''' recursively compute the maximum element in a sequence '''
    if not isinstance(lst, (list, set, str)) or not lst or \
    any(not isinstance(x, (str, int, float)) for x in lst):
        raise ValueError('Invalid Input')
    else:
        if start == stop:
            return lst[start]
        elif stop - start == 1:
            return lst[start] if lst[start] > lst[stop] else lst[stop]
        else:
            # binary recursion
            mid = (start + stop)//2
            lst = [maximum(lst, start, mid), maximum(lst, mid+1, stop)]
            return maximum(lst, 0, 1)

            # or linear recursion
            # return maximum([lst[start], maximum(lst, start+1, stop)], 0 ,1)


class TestMaximum(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaisesRegex(ValueError, 'Invalid Input'):
            maximum([], 0, 4)

    def test_maximum(self):
        self.assertEqual(maximum([0, 1, 2, 3, 2, 5, 14, 2], 0, 7), 14)

if __name__ == '__main__':
    unittest.main()
