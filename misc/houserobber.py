import unittest


def robber(houses):
	''' House robber: Maximum profit without alerting the police
	Rule: you cannot rob two adjacent houses!
	'''

	def maxSum(lst, start):
		''' returns the maximum sum of non adjacents given a list '''
		end = len(lst) - 1

		if start == end:
			return lst[start]
		elif end - start == 1:
			return max( lst[start], lst[end] )
		else:
			lst = lst[start:] # slice of input list
			first = lst[0] + maxSum(lst, 2) # including the first value in segment
			second = maxSum(lst, 1) # excluding the first value in segment

			return max(first, second)

	# control
	if not isinstance(houses, list) or len(houses) == 0 or any(not isinstance(house, int) for house in houses):
		raise Exception('Invalid input')
	else:
		return maxSum(houses, 0)


class TestRob(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			robber('')

		with self.assertRaisesRegex(Exception, 'Invalid input'):
			robber([1,2,3,'3'])
	def test_no_house_to_rob(self):
		self.assertEqual(robber([100]), 100)

	def test_rob_maximum(self):
		self.assertEqual(robber([8, 4, 1, 9]), 17)
		self.assertEqual(robber([1,2,3,4,5,6,7,8]), 20)
		self.assertEqual(robber([8,4,1,9,3,7,2]), 24)
		self.assertEqual(robber([10, 40, 30, 20]), 60)
		self.assertEqual(robber([10, 100, 20]), 100)

if __name__ == '__main__':
	unittest.main()
