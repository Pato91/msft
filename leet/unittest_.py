import unittest

class TestCases(unittest.TestCase):
	def test_something(self):
		self.assertTrue(something())
		self.assertEqual(something(), value)
		with self.assertRaisesRegex(Exception, 'Error message'):
			something()
