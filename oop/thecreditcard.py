import unittest

class CreditCard(object):
	"""a consumer Credit Card"""
	def __init__(self, customer='', bank='', account='', limit=0):
		''' create a template card with attributes

		customer: Customer name i.e Victor Kanyii
		bank: Name of the bank i.e Equity Bank
		account: Account identifier i.e 1180171207105
		limit:  Credit limit

		initial balance is zero
		'''
		super(CreditCard, self).__init__()
		self._customer = customer
		self._bank = bank
		self._account = account
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		''' return name of customer '''
		return self._customer

	def get_bank(self):
		''' return banks name '''
		return self._bank

	def get_account(self):
		''' return the account identifying number '''
		return self._account

	def get_balance(self):
		''' return current balance '''
		return self._balance

	def get_limit(self):
		''' return the current credit limit '''
		return self._limit

	def charge(self, price):
		''' charge the given price to card assuming sufficient credit limit 

		return False if charge exceeds the current limit
		return True if making a charge is possible
		'''
		# TODO : robust type checking and error handling
		if price + self._balance > self._limit:
			return False
		self._balance += price
		return True

	def make_payment(self, amount):
		''' process customer payment to reduce or offset the credit balance '''
		# TODO : robust type checking and error handling
		self._balance -= amount
		return


class TestCreditCard(unittest.TestCase):
	def test_create_credit_card(self):
		self.assertTrue(CreditCard())
		self.assertTrue(CreditCard('Karen Mwikali', 'Co-operative Bank', '01108172976100', 1000))

	def test_card_has_attributes(self):
		''' all attributes below are encapsulated and should not be accessed directly '''
		card = CreditCard()
		self.assertEqual(card._customer, '')
		self.assertEqual(card._bank, '')
		self.assertEqual(card._account, '')
		self.assertEqual(card._limit, 0)
		self.assertEqual(card._balance, 0)

	def test_card_has_methods(self):
		''' class interface: the methods '''
		card = CreditCard()
		self.assertEqual(card.get_customer(), '')
		self.assertEqual(card.get_bank(), '')
		self.assertEqual(card.get_account(), '')
		self.assertEqual(card.get_balance(), 0)
		self.assertEqual(card.get_limit(), 0)
		self.assertEqual(card.charge(0), True)
		self.assertEqual(card.make_payment(0), None)

if __name__ == '__main__':
	unittest.main()
