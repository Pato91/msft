import unittest

def binarysum(lst, start, stop):
    ''' compute the sum of elements in a list through binary recursion
    start: lowest index in an array or array segment
    stop: highest inex in an array: len(array)-1
    runtime: O(n) linear
    space: O(log n) :)
    '''
    if not isinstance(lst, list) or not lst \
    or any(not isinstance(x, (int, float)) for x in lst+[start, stop]):
        raise ValueError('Invalid input')
    else:
        if start > stop:
            return 0
        elif start == stop:
            return lst[start]
        else:
            mid = (start+stop)//2
            return binarysum(lst, start, mid) + binarysum(lst, mid+1, stop)


class TestSum(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaisesRegex(ValueError, 'Invalid input'):
            binarysum('1ndsa', 0, 5)

    def test_sum(self):
        self.assertEqual(binarysum([1, 2, 3, 4, 5, 6], 0, 5), 21)
        self.assertEqual(binarysum([1, 2, 3, 4, 5, 6, 7], 0, 6), 28)


if __name__ == '__main__':
    unittest.main()
