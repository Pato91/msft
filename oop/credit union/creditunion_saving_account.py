import unittest
from creditunion_account import Account
import math

class SavingAccount(Account):
	"""A customer SavingAccount"""
	def __init__(self, owner='', rate=0.5):
		''' Create a new saving account
		rate: Monthly percentage interest rates earned by savings
		target: Saving target, default is 100 dollars
		_mode: savings mode: can be
			open - withdraw at any time,
			lock - withdrawal open when target is passed
			fixed - save for a time period
		:TODO: implement modes and withdrawal conditions
		'''
		super().__init__(owner, atype='saving')
		self._rate = rate
		self._target = 100

	def _compute_interest(self):
		''' compute and add monthly interest to savings
		should only be triggered when generating monthly report
		'''
		self._balance *= ((100+self._rate)/100)

	def set_target(self, amount):
		''' sets a savings goal '''
		self._target = amount

	def get_target(self):
		return self._target

	def get_balance_to_target(self):
		return self._target - self._balance
		
class TestSavingAccount(unittest.TestCase):
	def test_create_account(self):
		self.assertTrue(SavingAccount())

	def test_compute_interest(self):
		account = SavingAccount()
		account.deposit(1000)
		account._compute_interest()
		self.assertEqual(math.ceil(account.get_balance()), 1005)

	def test_set_and_get_target(self):
		account = SavingAccount()
		account.set_target(10000)
		self.assertEqual(account.get_target(), 10000)

	def test_get_balance_to_target(self):
		account = SavingAccount()
		account.set_target(10000)
		account.deposit(2000)
		self.assertEqual(account.get_balance_to_target(), 8000)


if __name__ == '__main__':
	unittest.main()
