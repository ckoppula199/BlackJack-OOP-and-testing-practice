import BlackJack
import unittest

class CardTest(unittest.TestCase):

	def setUp(self):
		self.card = BlackJack.Card(8, 3)

	def test_card_is_as_expected(self):
		self.assertEqual(self.card.show(), "The 8 of Spades")


if __name__ == "__main__":
	unittest.main()