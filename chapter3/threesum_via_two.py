import unittest

def twoSum(lst, target, skip=-1):
	''' generates pairs of numbers whose sum is the target '''
	pairs = []
	hash = set()
	for i in range(len(lst)):
		if i == skip:
			continue

		diff = target - lst[i]
		if diff not in hash:
			hash.add(lst[i])
			continue

		pair = [diff, lst[i]]
		pair.sort()
		if pair not in pairs:
			pairs.append(pair)

	return pairs


def threeSum(lst):
	''' generates triplets of numbers whose sum is zero '''
	if not isinstance(lst, list) or len(lst) < 3 or any(not isinstance(x, (int, float)) for x in lst):
		raise Exception('Invalid Input')

	elif len(lst) == 3:
		if sum(lst) == 0:
			lst.sort()
			return lst
		return []

	else:
		triplets = []
		# generate triplets
		for i in range(len(lst)):
			target = -1*lst[i]
			pairs = twoSum(lst, target, i) #skip index i in generating pairs

			if pairs:
				for pair in pairs:
					pair.append(lst[i])
					pair.sort()

					if pair not in triplets:
						triplets.append(pair)

		return triplets


class Tests(unittest.TestCase):
	def test_invalid_inputs(self):
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			threeSum(1)
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			threeSum([])
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			threeSum(['1','2',3])

	def test_two_sum(self):
		self.assertEqual(twoSum([-1,0,1,1,2],2), [[1,1],[0,2]])
		self.assertEqual(twoSum([1, 3, 2, 5, 9], 7), [[2, 5]])
		self.assertEqual(twoSum([-1,0,1,1,2],-5), [])

	def test_length_of_three(self):
		self.assertEqual(threeSum([0,-1,1]), [-1,0,1])
		self.assertEqual(threeSum([0,-1,3]), [])

	def test_threesum(self):
		self.assertEqual(threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])
		self.assertEqual(threeSum([-1,0,1,1,2,3,-2,-4]), [[-1,0,1], [-2,-1,3], [-2,0,2], [-2,1,1], [-4,1,3]])

if __name__ == '__main__':
	unittest.main()
