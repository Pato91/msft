import unittest


class Vector(object):
	""" represent a Vector in multidimensional space 

	TODO: represent multidimension vectors 
	"""
	def __init__(self, dimension):
		''' create a vector of given dimension '''
		super(Vector, self).__init__()
		self._coords = [0] * dimension

	def __len__(self):
		''' return the dimenson of a vector '''
		return len(self._coords)

	def __getitem__(self, index):
		''' return element at given index of vector '''
		return self._coords[index]

	def __setitem__(self, index, value):
		''' sets the vector index to value '''
		self._coords[index] = value

	def __add__(self, other):
		''' returns sum of two vectors '''
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for i in range(len(self)):
			result[i] = self[i] + other[i]
		return result

	def __eq__(self, other):
		''' qualify equality between two vectors '''
		return self._coords == other._coords

	def __ne__(self, other):
		''' qualify inequality between two vectors '''
		return not self == other

	def __str__(self):
		''' generate string representation of vector '''
		return '< ' + str(self._coords)[1:-1] + ' >'



class TestVector(unittest.TestCase):
	def test_create_vector(self):
		self.assertTrue(Vector(2))

	def test_get_vector_length(self):
		vector = Vector(2)
		self.assertEqual(len(vector), 2)

	def test_get_vector_item(self):
		vector = Vector(2)
		self.assertEqual(vector[1], 0)

	def test_set_vector_item(self):
		vector = Vector(2)
		vector[1] = 5
		self.assertEqual(vector[1], 5)

	def test_add_vectors(self):
		first = Vector(2)
		first[1] = 12
		second = Vector(2)
		second[1] = 8

		third = first + second
		self.assertEqual(third[1], 20)

	def test_equality_check(self):
		first = Vector(2)
		second = Vector(2)
		self.assertTrue(first == second)
		self.assertTrue(first.__eq__(second))
		second[0] = 5
		self.assertTrue(first != second)
		self.assertTrue(first.__ne__(second))

	def test_adapted_representation(self):
		vector = Vector(2)
		self.assertEqual(vector.__str__(), '< 0, 0 >')


if __name__ == '__main__':
	unittest.main()
