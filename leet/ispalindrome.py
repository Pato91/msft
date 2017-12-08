def _reverse(number):
	rev = 0
	while number > 0:
		rev = rev*10 + number%10
		number //= 10
	return rev

def isPalindrome(number):
	""" check is a number is a palindrome """
	if not isinstance(number, int) or number < 0 or number >= 1000000:
		raise Exception('invalid input')
	elif number < 10:
		return True
	else:
		while True:
			rev = _reverse(number)
			if rev == number:
				return True
			number += _reverse(number)
			if number > 1000000:
				return False

print(isPalindrome(33))
print(isPalindrome(0))
print(isPalindrome(121))
print(isPalindrome(999999))
print(isPalindrome(999998))
# print(isPalindrome(1000001))
# print(isPalindrome(-30))
# print(isPalindrome(-30.0))