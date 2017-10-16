import unittest

def maxFour(arr):
	'''Returns maximum sum of any four consecutive elements
	given an array of numbers, determine the maximum sum of four consecutive elements
	'''
	# Using sliding window technique, length = 4, loop through inner sub array of four and get sum

	# start = 0
	# length = 4
	# max_ = 0

	# for i in range(length, len(arr)+1):
	# 	sum_ = sum(arr[start: i])
	# 	if sum_ > max_:
	# 		max_ = sum_
	# 	start +=1

	# Running sum technique, use previous sum of four |: runtime O(n)
	start = 0
	length = 4
	max_ = sum(arr[start: length])

	for i in range(length, len(arr) ):
		start +=1
		sum_ = max_+arr[i]-arr[start]
		if sum_ > max_:
			max_ = sum_

	return max_


class Test(unittest.TestCase):
	def test_maximum(self):
		self.assertEqual(maxFour([1, 2, 2, 8, 1]), 13)
		self.assertEqual(maxFour([1, 2, 2, 8, 1, 7, 6, 6, 4]), 23)

if __name__ == '__main__':
	unittest.main()
