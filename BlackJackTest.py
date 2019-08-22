import Card
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
		self.assertEqual(self.card.show(), "8 of Spades")
		self.assertEqual(self.card2.show(), "King of Hearts")

	@logger
	def test_correct_show_format(self):
		self.assertNotEqual(self.card.show(), "The 8 of Spades")
		self.assertNotEqual(self.card.show(), "The Eight of Spades")
		self.assertNotEqual(self.card.show(), "Eight of Spades")

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




if __name__ == "__main__":
	unittest.main()