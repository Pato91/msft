import unittest


def zeroMatrix(matrix):
	""" Set all column and row values to zero for the column and row of a value found to be zero in the original matrix """

	def _zero(posn, flag):
		"""sets column and row values to zero depending on flag """
		if flag == 'back':
			cstart, cstop, cstep = posn[1]-1, -1, -1
			rstart, rstop, rstep = posn[0]-1, -1, -1
		else:
			cstart, cstop, cstep = posn[1]+1, n, 1
			rstart, rstop, rstep = posn[0]+1, m, 1

		for  i in range(rstart, rstop, rstep):
			if matrix[i][posn[1]] == 0:
				break
			matrix[i][posn[1]] = 0

		for  j in range(cstart, cstop, cstep):
			if matrix[posn[0]][j] == 0:
				break
			matrix[posn[0]][j] = 0


	m = len(matrix) # row count
	n = len(matrix[0]) # column count
	# m * n matrix

	stops = []

	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				_zero([i,j], 'back')
				stops.append([i,j])

	if stops:
		for p in stops:
			_zero(p, 'front')

	return matrix


class TestZeroedMatrix(unittest.TestCase):
	data = (
		[
			[1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ],[
	        [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])

	def test_zero(self):
		real = zeroMatrix(self.data[0])
		expected = self.data[1]

		self.assertEqual(real, expected)

if __name__ == '__main__':
	unittest.main()
