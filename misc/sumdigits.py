import unittest

def sumdigits(num):
    ''' sums all the digits in an integer number '''

    def getSum(num):
        ''' helper: compute sum of a number recursively
        : intdivision and modulo fun
        '''
        total = 0
        while num//10 >= 0:
            total += num%10 #add rightmost digit
            num //= 10 #then eliminate it
            if num == 0:
                break
        if total > 10: #can be added futher, recurse
            return getSum(total)
        return total

    #
    if not isinstance(num, int):
        raise Exception('Invalid input')
    elif 0 <= abs(num) < 10: #num in range -9 and 9
        return num
    elif num < 0:
        return -1*getSum( abs(num) )
    else:
        return getSum(num)


class Test(unittest.TestCase):
    def test_invalid(self):
        with self.assertRaisesRegex(Exception, 'Invalid input'):
            sumdigits('1bcd')

    def test_single_digit(self):
        self.assertEqual(sumdigits(1), 1)
        self.assertEqual(sumdigits(-1), -1)

    def test_long_sum(self):
        self.assertEqual(sumdigits(12345), 6)
        self.assertEqual(sumdigits(10000), 1)
        self.assertEqual(sumdigits(-10000), -1)

if __name__ == '__main__':
    unittest.main()

'''
# given a number, add all digits until result is a single digit
handle single digit input: 5 - return number immediately
handle invalid input , NAN - raise an exception or return None?
handle normal case long input: 12342
negative numbers? -123?

output? return sum?
use a data structure? list?

solution steps:

1: validate input

2: convert number to string *
3: check length of string - 1? - return number *
4: more: pick each str element *
5 convert to number *
6 add to running sum
9 repeat from step 2, num is sum

q: without converting to string
q: how to iterate over an integer?

# sum = 0
2: check if num < 10: return num
3: more? iterate over integer
- num%10 to get rightmost
- num // 10 eliminates rightmost
do until num//10 is zero
6: add to running sum

'''
