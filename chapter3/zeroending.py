import unittest

def zeroEnding(lst):
	''' moves zeros in a list to the end of the list '''
	if not isinstance(lst, list) or len(lst) < 1 or any(not isinstance(x, (int, float)) for x in lst):
		raise Exception('Invalid Input')
	elif 0 not in lst:
		return None
	else:
		while True:
			index = lst.index(0)
			if any(x > 0 for x in lst[index+1:]):
				lst.remove(0)
				lst.append(0)
			else:
				return lst

class Tests(unittest.TestCase):
	def test_null_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			zeroEnding(1)

	def test_without_zero(self):
		self.assertEqual(zeroEnding([1]), None)

	def test_zero_ending(self):
		self.assertEqual(zeroEnding([0, 2, 1, 0]), [2, 1, 0, 0])

if __name__ == '__main__':
	unittest.main()
