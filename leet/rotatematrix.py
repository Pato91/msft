import unittest

def aRotate(M):
	""" rotate a matrix M by 90 degrees anticlockwise """
	n = len(M)
	MP = [] # rotated matrix, n*n

	for i in range(n-1, -1, -1): # iterate over rows backwards
		R = [] # rotated rows
		for j in range(n):
			R.append(M[j][i])
		MP.append(R)
	return MP

def cRotate(M):
	""" rotate a matrix M by 90 degrees clockwise """
	n = len(M)
	MP = [] # rotated matrix, n*n

	for i in range(n):
		R = [] # rotated rows
		for j in range(n-1, -1, -1): # iterate over rows backwards
			R.append(M[j][i])
		MP.append(R)
	return MP

class TestRotate(unittest.TestCase):
	data = (
		[
			[1, 0, 0, 2],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[3, 0, 0, 4]
		],[
			[3, 0, 0, 1],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[4, 0, 0, 2]
		],[
			[2, 0, 0, 4],
			[0, 0, 0, 0],
			[0, 0, 0, 0],
			[1, 0, 0, 3]
		])

	def test_rotate_clockwise(self):
		rotated = cRotate(self.data[0])
		expected = self.data[1]
		self.assertEqual(rotated, expected)

	def test_rotate_anticlockwise(self):
		rotated = aRotate(self.data[0])
		expected = self.data[2]
		self.assertEqual(rotated, expected)

if __name__ == '__main__':
	unittest.main()
