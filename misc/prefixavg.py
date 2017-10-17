import unittest

def prefixAvg(lst):
	''' Compute the prefix averages of each element in an input list '''
	if not isinstance(lst, list) or len(lst) == 0 or any(not isinstance(x, (int, float)) for x in lst ):
		raise TypeError('input must be a valid sequence of numbers')
	elif len(lst) == 1:
		return lst
	else:
		total = 0
		avgs = []
		for i in range(len(lst)):
			total += lst[i]
			avgs.append( total/(i+1) )
		return avgs


class Test(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(TypeError, 'input must be a valid sequence of numbers'):
			prefixAvg('acsd')
		with self.assertRaisesRegex(TypeError, 'input must be a valid sequence of numbers'):
			prefixAvg([1,2,3,'z'])

	def test_prefix_avg(self):
		self.assertEqual(prefixAvg([1]), [1])
		self.assertEqual(prefixAvg([1,2,3,4]), [1.0,1.5,2.0,2.5])


if __name__ == '__main__':
	unittest.main()
