import unittest
from thecreditcard import CreditCard

class PredatorCard(CreditCard):
	"""docstring for PredatorCard"""
	def __init__(self, customer='', bank='', account='', limit=0, apr=0):
		''' create a new instance of the predatory credit card class

		customer: Customer name i.e Victor Kanyii
		bank: Name of the bank i.e Equity Bank
		account: Account identifier i.e 1180171207105
		limit:  Credit limit
		apr: Annual percentage rate of interest

		initial balance is zero
		'''
		super().__init__(customer, bank, account, limit) # call super constructor
		self._apr = apr

	def charge(self, price):
		''' charge given price to card assuming sufficient credit limit
		return True if charge processed
		return False and assess $5 fee if charge denied
		'''
		success = super().charge(price)
		if not success:
			self._balance += 5 # assess the penalty
		return success

	def process_interest(self):
		''' assess the monthy interest on outstanding balance 
		return balance plus interst
		'''
		if self._balance > 0:
			monthly_factor = pow(1 + self._apr, 1/12)
			self._balance *= monthly_factor

		
class TestPredatorCard(unittest.TestCase):

	def test_create_card(self):
		self.assertTrue(PredatorCard())

	def test_card_has_attributes(self):
		''' test predator card inheritsattributes from the parent class '''
		card = PredatorCard()
		self.assertEqual(card._customer, '')
		self.assertEqual(card._bank, '')
		self.assertEqual(card._account, '')
		self.assertEqual(card._limit, 0)
		self.assertEqual(card._balance, 0)
		self.assertEqual(card._apr, 0)

	def test_card_has_properties(self):
		card = PredatorCard()
		self.assertEqual(card.get_customer(), '')
		self.assertEqual(card.get_bank(), '')
		self.assertEqual(card.get_account(), '')
		self.assertEqual(card.get_balance(), 0)
		self.assertEqual(card.get_limit(), 0)
		self.assertEqual(card.make_payment(0), None)
		self.assertEqual(card.charge(0), True)

	def test_penalize_overcharge(self):
		card = PredatorCard()
		self.assertEqual(card.get_balance(), 0)
		card.charge(15) #charge exceeds limit: fail and penalize $5
		self.assertEqual(card.get_balance(), 5)

	def test_monthly_interest_on_balance(self):
		card = PredatorCard(apr=5) #balance of zero, default
		card.charge(100) #will raise balance to $5
		card.charge(100) #will raise balance to $10
		# this is unsuitable, implement a set_balance() method in the CreditCard
		self.assertEqual(card.get_balance(), 10)
		card.process_interest() #compute balance plus interest
		self.assertTrue(card.get_balance(), 10*pow(1+5, 1/12))


if __name__ == '__main__':
	unittest.main()
