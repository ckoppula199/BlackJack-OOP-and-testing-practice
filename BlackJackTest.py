import BlackJack
import unittest
from UserDefinedExceptions import *

class CardTest(unittest.TestCase):

	def setUp(self):
		self.card = BlackJack.Card(8, 3)

	def test_card_is_as_expected(self):
		self.assertEqual(self.card.show(), "8 of Spades")

	def test_correct_show_format(self):
		self.assertNotEqual(self.card.show(), "The 8 of Spades")
		self.assertNotEqual(self.card.show(), "The Eight of Spades")
		self.assertNotEqual(self.card.show(), "Eight of Spades")

	def test_out_of_bounds_error(self):
		with self.assertRaises(CardException):
			self.card = BlackJack.Card(4, 4) # suit out of range
			self.card = BlackJack.Card(29, 2) # rank out of range
			self.card = BlackJack.Card(39, 23) # rank and suit out of range



if __name__ == "__main__":
	unittest.main()