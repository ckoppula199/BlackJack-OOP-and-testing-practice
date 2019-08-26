from Card import Card
from CardCollections import *
from Players import *
import unittest
from unittest.mock import patch
from UserDefinedExceptions import *
import logging
from BlackJack import Blackjack

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
		self.card = Card(8, 3)
		self.card2 = Card(13, 2)

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
			Card(4, 4)

	@logger
	def test_rank_out_of_bounds_error(self):
		with self.assertRaises(CardException):
			Card(29, 2)

	@logger
	def test_rank_and_suit_out_of_bounds_error(self):
		with self.assertRaises(CardException):
			Card(39, 23)

	@logger
	def test_get_card_value(self):
		self.assertEqual(self.card.get_card_value(), 8)
		self.assertEqual(self.card2.get_card_value(), 10)
		ace = Card(14, 3)
		self.assertEqual(ace.get_card_value(), 11)


class CardCollectionTest(unittest.TestCase):

	def setUp(self):
		self.draw_pile = CardCollection("Draw Pile")
		for i in range(2, 15):
			card = Card(i, 2)
			self.draw_pile.add_card(card)

	@logger
	def test_add_card(self):
		card = Card(12, 1)
		self.draw_pile.add_card(card)
		self.assertEqual(self.draw_pile.cards[-1], card) #check if last card added is last card in deck

	@logger
	def test_only_accepts_card(self):
		card = Card(3,2)
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
		self.assertEqual(13, self.draw_pile.get_size())

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

class DeckTest(unittest.TestCase):

	def setUp(self):
		self.deck = Deck("Deck")

	@logger
	def test_populate(self):
		self.assertEqual(self.deck.get_size(), 52)
		for i in range(self.deck.get_size()):
			for j in range(self.deck.get_size()):
				if i == j:
					continue
				self.assertFalse(str(self.deck.cards[i]) == str(self.deck.cards[j]))

class HandTest(unittest.TestCase):
	 def setUp(self):
	 	self.hand = Hand("Hand")

	 @logger
	 def test_display(self):
	 	deck = Deck("Deck")
	 	deck.deal(self.hand, 3)
	 	self.hand.display()

class PlayerTest(unittest.TestCase):

	 def setUp(self):
	 	self.player = Player("player")
	 	self.deck = Deck("deck")
	 	self.deck.deal(self.player.hand, 2)

	 @logger
	 def test_get_score(self):
	 	self.assertEqual(21, self.player.get_score())

	 @logger
	 def test_get_hand_size(self):
	 	self.assertEqual(2, self.player.get_hand_size())

	 @logger
	 def test_draw(self):
	 	self.assertTrue(self.player.draw(self.deck))
	 	self.player.hand.remove_card()
	 	self.player.hand.remove_card()
	 	self.assertFalse(self.player.draw(self.deck))

	 @logger
	 def test_check_if_bust(self):
	 	self.player.hand.remove_card()
	 	self.player.hand.remove_card()
	 	self.assertFalse(self.player.check_if_bust())
	 	self.player.draw(self.deck)
	 	self.player.draw(self.deck)
	 	self.player.draw(self.deck)
	 	self.player.draw(self.deck)
	 	self.assertTrue(self.player.check_if_bust())

class UserTest(unittest.TestCase):
	
	def setUp(self):
		self.ace = Card(14, 3)
		self.king = Card(13, 2)
		self.user = User("User")
		self.deck = Deck("DrawPIle")

	@logger
	def test_validate_input_valid(self):
		self.assertTrue(self.user.validate_input("1"))
		self.assertTrue(self.user.validate_input("2"))

	@logger
	def test_validate_input_invalid(self):
		self.assertFalse(self.user.validate_input(1))
		self.assertFalse(self.user.validate_input(2))
		self.assertFalse(self.user.validate_input("one"))

	@logger
	def test_process_choice_2(self):
		self.assertFalse(self.user.process_choice("2", self.deck))

	@logger
	def test_process_choice_1_not_bust(self):
		self.assertFalse(self.user.process_choice("1", self.deck))

	@logger
	def test_process_choice_1_bust(self):
		self.user.hand.add_card(self.ace)
		self.user.hand.add_card(self.king)
		self.assertTrue(self.user.process_choice("1", self.deck))

	@logger
	def test_get_user_input_1(self):
		with patch('builtins.input', return_value="1"):
			self.assertEqual("1", self.user.get_user_input())

	@logger
	def test_get_user_input_2(self):
		with patch('builtins.input', return_value="2"):
			self.assertEqual("2", self.user.get_user_input())


class ComputerTest(unittest.TestCase):

	def setUp(self):
		self.ace = Card(14, 3)
		self.five = Card(5, 3)
		self.king = Card(13, 2)
		self.computer = Computer("Computer")
		self.deck = Deck("DrawPile")

	@logger
	def test_computer_turn_lt16(self):
		self.computer.hand.add_card(self.ace)
		self.computer.hand.add_card(self.king)
		self.assertFalse(self.computer.computer_turn(self.deck))
		self.assertTrue(self.computer.stick)

	@logger
	def test_computer_turn_gt16(self):
		self.computer.hand.add_card(self.five)
		self.assertFalse(self.computer.computer_turn(self.deck))
		self.assertFalse(self.computer.stick)

	@logger
	def test_computer_turn_goes_bust(self):
		self.computer.hand.add_card(self.ace)
		self.computer.hand.add_card(self.five)
		self.assertTrue(self.computer.computer_turn(self.deck))

#methods of this class mainly just wrap methods of previous classes
class BlackjackTest(unittest.TestCase):

	def setUp(self):
		self.blackjack = Blackjack()

	@logger
	def test_check_whos_bsut(self):
		self.assertTrue(self.blackjack.check_whos_bust(True, True))
		self.assertTrue(self.blackjack.check_whos_bust(False, True))
		self.assertTrue(self.blackjack.check_whos_bust(True, False))
		self.assertFalse(self.blackjack.check_whos_bust(False, False))



if __name__ == "__main__":
	unittest.main()