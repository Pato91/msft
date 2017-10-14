import unittest
from creditunion_account import Account

class CheckingAccount(Account):
	"""docstring for SavingAccount"""
	def __init__(self, owner=''):
		super().__init__(owner, atype='checking')
		
class TestSavingAccount(unittest.TestCase):
	def test_create_account(self):
		self.assertTrue(CheckingAccount())


if __name__ == '__main__':
	unittest.main()
