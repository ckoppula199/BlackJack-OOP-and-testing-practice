from Players import *
from CardCollections import *
from Card import Card

class Blackjack:

	def __init__(self):
		self.user = User("user")
		self.computer = Computer("computer")
		self.drawpile = Deck("drawpile")

	def initial_deal(self):
		pass

	def user_turn(self):
		pass

	def computer_turn(self):
		pass