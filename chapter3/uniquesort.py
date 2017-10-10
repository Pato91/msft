import unittest

def uniques(lst):
	''' removes duplicates from a sorted list '''

	n = 0 #track position

	while True:
		if n >= len(lst):
			break

		curr = lst[n-1]
		nxt = lst[n]
		if curr == nxt:
			lst.remove(curr)
		else:
			n+=1
	return len(lst)

class Tests(unittest.TestCase):
	def test_no_duplicate(self):
		self.assertEqual(uniques([1,2]), 2)

	def test_duplicates(self):
		self.assertEqual(uniques([1,1,2]), 2)

	def test_dupicates_and_more(self):
		self.assertEqual(uniques([1,1,1,1,1,2]), 2)

if __name__ == '__main__':
	unittest.main()