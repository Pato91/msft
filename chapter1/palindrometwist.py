def checkPalindrome(number):
	''' checks if a number is a palindrome and returns True otherwise returns False '''
	limit = 1000000 #upper bound when checking for palindrome

	def getReverse(number):
		''' returns the reverse of a number '''
		return int(str(number)[::-1])

	def isPalindrome(number):
		reverse = getReverse(number)
		if reverse == number:
			return True
		else:
			number += reverse
			if number > limit:
				return False
			return isPalindrome(number)

	if not isinstance(number, int):
		raise Exception('input must be a valid integer ')
	else:
		# check for palindrome
		if number < 0 or number > limit:
			return False
		if number >= 0 and number <= 9:
			return True
		else:
			return isPalindrome(number)


# test cases

# print(checkPalindrome('not a number')) # invalid input
# print(checkPalindrome(None)) # invalid input
print(checkPalindrome(1)) # single digits
print(checkPalindrome(121)) # palindrome case
print(checkPalindrome(33)) # same digit number
print(checkPalindrome(12)) # normal case?
print(checkPalindrome(999999)) # extreme case
print(checkPalindrome(999998)) # extreme case
