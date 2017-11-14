import unittest

def transpose(M):
    """ Generate the transpose of a matrix M """
    if not isinstance(M, list) or \
     any(not isinstance(row, list) for row in M):
        raise Exception('Invalid Input')
    else:
        rows = len(M)
        if rows == 0: # null matrix, empty
            return M
        cols = max(list(len(row) for row in M))
        if cols == 1: # 1x1 matrix
            return M
        elif any(len(row) < cols for row in M):  # unequal dimensions of rows in matrix
            raise Exception('Invalid Input')
        else:
            # T = [] # transpose matrix
            # for i in range(cols):
            #     T.append(list(M[r][i] for r in range(rows)))
            # return T

            # return [ [ M[r][i] for r in range(rows) ] for i in range(cols) ]

            return [ list(row) for row in zip(*M) ]


class TestTranspose(unittest.TestCase):
    def test_valid_inputs(self):
        with self.assertRaisesRegex(Exception, 'Invalid Input'):
            transpose("abcd") # input not a list
        with self.assertRaisesRegex(Exception, 'Invalid Input'):
            transpose(["abcd"]) # input not a matrix
        with self.assertRaisesRegex(Exception, 'Invalid Input'):
            transpose([[1,2,3], [1,2]]) # unequal dimensionality

    def test_empty_matrix(self):
        self.assertEqual(transpose([]), [])

    def test_transpose_1x1(self):
        self.assertEqual(transpose([[1]]), [[1]])

    def test_transpose_square_dimensions(self):
        self.assertEqual(transpose([[1,2], [4,5]]), [[1,4], [2,5]]) # T 2X2
        self.assertEqual(transpose([[1,2,3], [4,5,6], [7,8,9]]), [[1,4,7], [2,5,8], [3,6,9]]) # T 3X3

    def test_transpose_nonsquare_dimensions(self):
        self.assertEqual(transpose([[1,2,3]]), [[1], [2], [3]]) # T 1X3
        self.assertEqual(transpose([[1,2,3], [4,5,6]]), [[1,4], [2,5], [3,6]]) # T 2X3


if __name__ == '__main__':
    unittest.main()
