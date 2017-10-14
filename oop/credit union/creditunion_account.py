import unittest
import time
from datetime import datetime

class Account(object):
	"""A bank Account"""
	def __init__(self, owner='', atype='checking'):
		''' Create a new account
		owner: The account owner i.e 'Jon Reese'
		type: Account type: can either be a savings or a checking account
		balance: The current account balance
		number: A random number sequence to identify the account
		logs: A list of all transactions made on the account
		'''
		super(Account, self).__init__()
		self._owner = owner
		self._type = atype
		self._balance = 0
		self._logs = []
		self._number = 'randomsequence'

		# log the account creation
		log = {
			'event': 'Account Created',
			'sec_time': self._gettime()[0],
			'str_time': self._gettime()[1],
			'balance': self._balance
		}
		self._logs.append( log )

	def _gettime(self):
		ts = time.time()
		ct = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		return ts, ct

	def _log(self, event):
		''' create a log for an event: TODO '''
		pass

	def get_owner(self):
		return self._owner

	def get_type(self):
		return self._type

	def get_balance(self):
		return self._balance

	def deposit(self, amount):
		self._balance += amount

	def withdraw(self, amount):
		if self._balance > amount:
			self._balance -= amount
		else:
			return 'Amount exceeds available balance'

	def get_account_statement(self):
		return '\n'.join('{tstamp} : {event}'.format(tstamp=log['str_time'], event=log['event']) for log in self._logs)


class TestAccount(unittest.TestCase):
	def test_create_account(self):
		self.assertTrue(Account())

	def test_get_owner(self):
		account = Account(owner='John Paul')
		self.assertEqual(account.get_owner(), 'John Paul')

	def test_get_type(self):
		account = Account(atype='saving')
		self.assertEqual(account.get_type(), 'saving')

	def test_get_balance(self):
		account = Account()
		self.assertEqual(account.get_balance(), 0)

	def test_get_statement(self):
		account = Account()
		time = account._gettime()[1]
		self.assertEqual(account.get_account_statement(), '{} : Account Created'.format(time))

	def test_make_deposit(self):
		account = Account()
		account.deposit(3000)
		self.assertEqual(account.get_balance(), 3000)

	def test_withdraw_amount(self):
		account = Account()
		account.deposit(3000)
		account.withdraw(1000)
		self.assertEqual(account.get_balance(), 2000)
		self.assertEqual(account.withdraw(4000), 'Amount exceeds available balance')


if __name__ == '__main__':
	unittest.main()
