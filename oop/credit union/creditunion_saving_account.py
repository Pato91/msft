import unittest
from creditunion_account import Account

class SavingAccount(Account):
	"""docstring for SavingAccount"""
	def __init__(self, owner='', rate=0.5):
		super().__init__(owner, atype='saving')
		self._rate = rate
		
class TestSavingAccount(unittest.TestCase):
	def test_create_account(self):
		self.assertTrue(SavingAccount())


if __name__ == '__main__':
	unittest.main()
