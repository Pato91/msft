import unittest

def getReverse(number):
	''' returns the reverse of a number '''
	# reversing an integer
	reverse = 0
	while(number != 0):
		reverse = reverse*10 + number%10
		number = int(number / 10)
	return reverse

	# using string conversion
	# return int(str(number)[::-1])

def isPalindrome(number, limit=1000000):
	reverse = getReverse(number)

	if reverse == number:
		return True
	else:
		number += reverse
		if number > limit:
			return False
		return isPalindrome(number, limit)

def checkPalindrome(number):
	''' checks if a number is a palindrome and returns True otherwise returns False '''
	limit = 1000000 #upper bound when checking for palindrome

	if not isinstance(number, int):
		raise Exception('input must be a valid integer ')
	else:
		# check for palindrome
		if number < 0 or number > limit:
			return False
		if number >= 0 and number <= 9:
			return True
		else:
			return isPalindrome(number, limit)

# test cases
class Tests(unittest.TestCase):
	def test_reverse(self):
		self.assertEqual(getReverse(1235), 5321)
		self.assertNotEqual(getReverse(1235), 1235)

	def test_palindrome_function(self):
		self.assertTrue(isPalindrome(33))
		self.assertFalse(isPalindrome(999998))

	def test_check_palindrome(self):
		self.assertTrue(checkPalindrome(1))
		self.assertTrue(checkPalindrome(100))
		self.assertFalse(checkPalindrome(999998))
		self.assertTrue(checkPalindrome(999999))
		with self.assertRaisesRegex(Exception, 'input must be a valid integer '):
			checkPalindrome(None)

if __name__ == '__main__':
	unittest.main()
