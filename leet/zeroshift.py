
import unittest

def shiftZeros(arr):
	""" returns the length of the longest substring without repeating characters """
	if not isinstance(arr, list):
		raise Exception('Invalid input')
	else:
		n = len(arr)

		if n <= 2:
			return arr

		for i in range(n):
			if arr[i] != 0:
				continue
			else:
				j = i+1
				while j < n:
					if arr[j] != 0 and arr[i] == 0:
						arr[i], arr[j] = arr[j], arr[i]
						break
					else:
						j += 1
						if j == n:
							return arr
		return arr


class TestSubs(unittest.TestCase):
	def test_trivial(self):
		self.assertEqual(shiftZeros([]), [])
		self.assertEqual(shiftZeros([1]), [1])
		self.assertEqual(shiftZeros([0]), [0])

	def test_scanned(self):
		self.assertEqual(shiftZeros([1,0,2,3,4,0]), [1,2,3,4,0,0])
		self.assertEqual(shiftZeros([0,0,1,0,0,0,0,2]), [1,2,0,0,0,0,0,0])

if __name__ == '__main__':
	unittest.main()