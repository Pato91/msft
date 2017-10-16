import unittest

class CaesarCipher(object):
	"""docstring for CaesarCipher"""
	def __init__(self, shift):
		super (CaesarCipher, self).__init__()
		self.shift = shift
		self.encoder = [None]*26
		self.decoder = [None]*26

		for e in range(26):
			self.encoder[e] = chr((e + self.shift)%26 + ord('A'))
			self.decoder[e] = chr((e - self.shift)%26 + ord('A'))

		self.foward_shift = ''.join(self.encoder)
		self.backward_shift = ''.join(self.decoder)

	def encrypt(self, message):
		return self.transform(message, self.encoder)

	def decrypt(self, message):
		return self.transform(message, self.decoder)

	def transform(self, original, code):
		msg = list(original)
		for m in range(len(msg)):
			if msg[m].isupper():
				c = ord(msg[m]) - ord('A')
				msg[m] = code[c] #shifted element
		return ''.join(msg)


class Tests(unittest.TestCase):
	def test_create_cipher(self):
		self.assertTrue(CaesarCipher(3))

	def test_encode(self):
		cipher = CaesarCipher(3)
		plain = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
		encrypted = "WKH HDJOH LV LQ SODB; PHHW DW MRH'V."
		self.assertEqual(cipher.encrypt(plain), encrypted)

	def test_decode(self):
		cipher = CaesarCipher(3)
		encrypted = "WKH HDJOH LV LQ SODB; PHHW DW MRH'V."
		plain = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
		self.assertEqual(cipher.decrypt(encrypted), plain)


if __name__ == '__main__':
	unittest.main()
