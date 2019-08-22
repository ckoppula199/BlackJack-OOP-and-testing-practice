import Card
from CardCollections import *
import unittest
from UserDefinedExceptions import *
import logging

# decorator to wrap around tests that stores results and arguments and name of each test run in a text file
def logger(test):
	logging.basicConfig(filename="Test-Logs.txt", level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info(" {} ran with args: {} and kwargs: {}".format(test.__name__, args, kwargs))

		try:
			result = test(*args, **kwargs)
			logging.info(" {} RAN SUCCESSFULY\n".format(test.__name__))
			return result
		except AssertionError:
			logging.info(" {} DID NOT RUN SUCCESSFULY\n".format(test.__name__))
			raise AssertionError
			
		
	return wrapper


class CardTest(unittest.TestCase):

	def setUp(self):
		self.card = Card.Card(8, 3)
		self.card2 = Card.Card(13, 2)

	@logger
	def test_card_is_as_expected(self):
		self.assertEqual(str(self.card), "8 of Spades")
		self.assertEqual(str(self.card2), "King of Hearts")

	@logger
	def test_correct_show_format(self):
		self.assertNotEqual(str(self.card), "The 8 of Spades")
		self.assertNotEqual(str(self.card), "The Eight of Spades")
		self.assertNotEqual(str(self.card), "Eight of Spades")

	@logger
	def test_suit_out_of_bounds_error(self):
		with self.assertRaises(CardException):
			Card.Card(4, 4)

	@logger
	def test_rank_out_of_bounds_error(self):
		with self.assertRaises(CardException):
			Card.Card(29, 2)

	@logger
	def test_rank_and_suit_out_of_bounds_error(self):
		with self.assertRaises(CardException):
			Card.Card(39, 23)

	@logger
	def test_get_card_value(self):
		self.assertEqual(self.card.get_card_value(), 8)
		self.assertEqual(self.card2.get_card_value(), 10)


class CardCollectionTest(unittest.TestCase):

	def setUp(self):
		self.draw_pile = CardCollection("Draw Pile")
		for i in range(2, 14):
			card = Card.Card(i, 2)
			self.draw_pile.add_card(card)

	@logger
	def test_add_card(self):
		card = Card.Card(12, 1)
		self.draw_pile.add_card(card)
		self.assertEqual(self.draw_pile.cards[-1], card) #check if last card added is last card in deck

	@logger
	def test_only_accepts_card(self):
		card = Card.Card(3,2)
		self.draw_pile.add_card(card)
		self.draw_pile.add_card(2)
		self.draw_pile.add_card("Card")
		self.assertFalse(2 in self.draw_pile.cards)
		self.assertFalse("Card" in self.draw_pile.cards)
		self.assertTrue(card in self.draw_pile.cards)


	@logger
	def test_remove_card_mid(self):
		mid_card = self.draw_pile.cards[4]
		self.draw_pile.remove_card(4)
		self.assertFalse(mid_card in self.draw_pile.cards)

	@logger
	def test_remove_card_start(self):
		start_card = self.draw_pile.cards[0]
		self.draw_pile.remove_card(0)
		self.assertFalse(start_card in self.draw_pile.cards)

	@logger
	def test_remove_card_mid(self):
		end_card = self.draw_pile.cards[-1]
		self.draw_pile.remove_card(-1)
		self.assertFalse(end_card in self.draw_pile.cards)

	@logger
	def test_remove_card_return_value(self):
		card7 = self.draw_pile.cards[7]
		returned_card = self.draw_pile.remove_card(7)
		self.assertEqual(card7, returned_card)
		self.assertFalse(card7 in self.draw_pile.cards)

	@logger
	def test_size(self):
		self.assertEqual(12, self.draw_pile.get_size())

	@logger
	def test_is_empty(self):
		self.assertFalse(self.draw_pile.is_empty())
		self.assertTrue(CardCollection("temp").is_empty())

	@logger
	def test_swap_cards(self):
		first = self.draw_pile.cards[0]
		last = self.draw_pile.cards[-1]
		self.draw_pile.swap_cards(0, -1)
		self.assertEqual(first, self.draw_pile.cards[-1])
		self.assertEqual(last, self.draw_pile.cards[0])

	@logger
	def test_deal(self):
		hand = CardCollection("Hand")
		one = self.draw_pile.cards[-1]
		two = self.draw_pile.cards[-2]
		three = self.draw_pile.cards[-3]
		self.draw_pile.deal(hand, 3)
		self.assertEqual([one, two, three], hand.cards)





if __name__ == "__main__":
	unittest.main()