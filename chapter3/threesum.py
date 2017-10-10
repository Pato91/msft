import unittest

def threeSum(lst):
	''' from a list, get triplets that adds to zero '''
	if not isinstance(lst, list) or len(lst) < 3:
		raise Exception('Invalid Input')

	elif len(lst) == 3:
		if sum(lst) == 0:
			return lst
		return []

	else:
		triplets = []
		i = 0
		j = 1
		while j < len(lst):
			_sum = lst[i] + lst[j]
			diff = 0 - _sum
			if diff in lst[j+1 : ]:
				triplet = [lst[i], lst[j], diff]
				triplet.sort()
				if triplet not in triplets:
					triplets.append(triplet)
			j+=1
		return triplets

class Tests(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			threeSum([])

	def test_length_of_three(self):
		self.assertEqual(threeSum([-1, 0, 1]), [-1, 0, 1])
		self.assertEqual(threeSum([-1, 0, 2]), [])

	def test_triplets(self):
		self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

if __name__ == '__main__':
	unittest.main()
