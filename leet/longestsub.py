
import unittest

def longestSub(string):
	""" returns the length of the longest substring without repeating characters """
	if not isinstance(string, str):
		raise Exception('Invalid input')
	else:
		n = len(string)
		if n <= 1:
			return n

		sub = set()
		most = 0

		for c in string:
			if c not in sub:
				sub.add(c)
			else:
				m = len(sub)
				most = m if m > most else most
				sub.clear()
				sub.add(c)
		return most

class TestSubs(unittest.TestCase):
	def test_trivial(self):
		self.assertEqual(longestSub(''), 0)
		self.assertEqual(longestSub('a'), 1)

	def test_scanned(self):
		self.assertEqual(longestSub('aaaa'), 1)
		self.assertEqual(longestSub('abca'), 3)

if __name__ == '__main__':
	unittest.main()