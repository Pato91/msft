import unittest
import time
from creditunion import SavingAccount, CheckingAccount


class Customer(object):
	"""A bank Customer"""
	def __init__(self, name='', type='individual'):
		''' Create a bank customer
		name: Name of customer i.e 'Derek John'
		type: Type of a customer, can be a business or individual
		'''
		super(Customer, self).__init__()
		self._name = name
		self._type = type
		self._saving_account = None
		self._checking_account = None
		self._id = 'random'

	def get_name(self):
		return self._name

	def get_type(self):
		return self._type

	def get_account(self, atype):
		if atype == 'saving':
			return self._saving_account
		elif atype == 'checking':
			return self._checking_account
		return None

	def create_account(self, atype):
		''' creates an account of type atype '''
		if atype == 'saving' and self._saving_account is None:
			self._saving_account = SavingAccount()
		elif atype == 'checking' and self._checking_account is None:
			self._checking_account = CheckingAccount()
		return 'You already have a {} account'.format(atype) # or handle invalid accoutn type

	def get_account_balance(self, atype):
		''' returns the checking account balance '''
		balance = None
		if atype == 'checking':
			if self._checking_account:
				balance = self._checking_account.get_balance()
				return balance
		elif atype == 'saving':
			if self._saving_account:
				balance = self._saving_account.get_balance()
				return balance
		return None, 'You dont have a {} account'.format(atype)

	def get_overall_balance(self):
		''' returns the cobined balance of customers accounts '''
		savings_balance = self.get_account_balance('saving')
		checking_balance = self.get_account_balance('checking')
		if isinstance(savings_balance, (int, float)) and isinstance(checking_balance, (int, float)):
			return savings_balance + checking_balance
		elif isinstance(savings_balance, (int, float)):
			return savings_balance
		elif isinstance(checking_balance, (int, float)):
			return checking_balance
		return 'You have no active Accounts'

	def make_deposit(self, atype, amount):
		''' Makes a deposit in specified account: 
		If account doesnt exist, create one with initial amount specified
		'''
		if atype == 'saving':
			if not self._saving_account: #if account doesnt exist
				self.create_account(atype) #create account
			self._saving_account.deposit(amount)
		elif atype == 'checking':
			if not self._checking_account: #if account doesnt exist
				self.create_account(atype) #create account
			self._checking_account.deposit(amount)
		return 'Failed, you can only deposit in a saving or checking account'

	def withdraw(self, atype, amount):
		''' Withdraws amount from specified account '''
		account = self.get_account(atype)
		if account:			
			return account.withdraw(amount)


class TestCustomer(unittest.TestCase):
	def test_create_customer(self):
		self.assertTrue(Customer())

	def test_get_name(self):
		customer = Customer(name = 'Derek Jones')
		self.assertEqual(customer.get_name(), 'Derek Jones')

	def get_type(self):
		customer = Customer(type = 'Business')
		self.assertEqual(customer.get_type(), 'Business')

	def test_get_account(self):
		customer = Customer()
		self.assertEqual(customer.get_account('saving') ,None)
		self.assertEqual(customer.get_account('checking') ,None)

	def test_create_account(self):
		customer = Customer()
		customer.create_account('checking')
		self.assertTrue(customer.get_account('checking'))
		self.assertFalse(customer.get_account('saving'))
		customer.create_account('saving')
		self.assertTrue(customer.get_account('saving'))
		self.assertEqual(customer.create_account('checking'), 'You already have a checking account')
		self.assertEqual(customer.create_account('saving'), 'You already have a saving account')

	def test_get_account_balance(self):
		customer = Customer()
		self.assertEqual(customer.get_account_balance('checking')[1], 'You dont have a checking account')
		self.assertEqual(customer.get_account_balance('saving')[1], 'You dont have a saving account')
		self.assertEqual(customer.get_overall_balance(), 'You have no active Accounts')

	def test_make_deposit(self):
		customer = Customer()
		customer.make_deposit('saving', 5000)
		self.assertEqual(customer.get_account_balance('saving'), 5000)
		customer.make_deposit('checking', 2000)
		self.assertEqual(customer.get_overall_balance(), 7000)

	def test_make_withdrawal(self):
		customer = Customer()
		customer.create_account('saving')
		customer.make_deposit('saving', 7000)
		customer.withdraw('saving', 6000)
		self.assertEqual(customer.get_account_balance('saving'), 1000)
		self.assertEqual(customer.withdraw('saving', 5000), 'Amount exceeds available balance')


if __name__ == '__main__':
	unittest.main()
