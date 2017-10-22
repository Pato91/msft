import unittest

def power(x, n):
	''' Example of linear recursion
	recursively implement the pow(x,y) method
	Runtime O(n) linear time, results in O(n) recursive calls
	'''
	if n == 0:
		return 1
	else:
		return x * power(x, n-1)

# even better :)
def power(x, n):
	''' raise x to power n
	Runtime is O(n) linear time
	results in O(log n) recursive calls, memory usage being O(log n)
	'''
	if n == 0:
		return 1
	else:
		partial = power(x, n//2)
		result = partial * partial
		if n%2 == 1:
			result *= x
		return result


class TestPower(unittest.TestCase):
	def test_invelid_input(self):
		pass

	def test_power_func(self):
		self.assertEqual(power(4, 4), pow(4,4))

if __name__ == '__main__':
	unittest.main()
