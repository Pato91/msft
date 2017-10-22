import unittest

def reverse(lst, start, stop):
	''' Example of a linear recursion
	reverse a list bu recursive methods
	Runtime, O(n)
	'''
	if start < stop:
		lst[start], lst[stop] = lst[stop], lst[start]
		reverse(lst, start+1, stop-1)
	return lst


class TestReverse(unittest.TestCase):
	def test_invelid_input(self):
		pass

	def test_reverse(self):
		self.assertEqual(reverse([1,2,3,4], 0, 3), [4,3,2,1])
		self.assertEqual(reverse([1,2,3,4,5], 0, 4), [5,4,3,2,1])

if __name__ == '__main__':
	unittest.main()
