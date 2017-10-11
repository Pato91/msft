import unittest

def twoSum(lst, target):
	''' returns a pair that adds up to the target '''
	if not isinstance(lst, list) or len(lst) < 2 or any(not isinstance(x, (int, float)) for x in lst) or not isinstance(target, (int, float)):
		raise Exception('Invalid Input')
	else:
		hash = set()
		for i in range(len(lst)):
			diff = target - lst[i]
			if diff in hash:
				return [diff, lst[i]]
			hash.add(lst[i])
		return []

class Tests(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid Input'):
			twoSum([], 4)

	def test_no_pair(self):
		self.assertEqual(twoSum([1, 2], 5), [])

	def test_pair(self):
		self.assertEqual(twoSum([1, 3, 2, 5, 9], 7), [2, 5])

while __name__ == '__main__':
	unittest.main()
