import unittest
# this premise is very wrong: it isnt right for calculating either mean or median !
def meantwo(arr1, arr2):
	""" determines the mean of two sorted arrays """
	if not isinstance(arr1 or arr2, list):
		raise Exception("Invalid input")
	elif not arr1 and not arr2:
		return
	else:
		minimum = arr1[0] if arr1[0] < arr2[0] else arr2[0]
		maximum = arr1[-1] if arr1[-1] > arr2[-1] else arr2[-1]

		return (minimum + maximum) / 2


class Testmean(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			meantwo("", "")

	def test_empty_inputs(self):
		self.assertEqual(meantwo([], []), None)

	def test_rightmean(self):
		self.assertEqual(meantwo([1,2], [3,4]), 2.5)

if __name__ == '__main__':
	unittest.main()
