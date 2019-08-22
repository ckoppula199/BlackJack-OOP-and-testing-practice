from UserDefinedExceptions import *

class Card:

	# list indexes used to determine what card is being used
	SUIT = ["Clubs", "Diamonds", "Hearts", "Spades"]

	# first 2 entries are None for convenience, so index 2 is 2, 3 is 3 etc
	RANK = [None, None, "2", "3", "4", "5", "6", "7", 
			"8", "9", "10", "Jack", "Queen", "King"]


	def __init__(self, rank, suit):
		# checks that card being created is valid
		if (rank >= 2 and rank <= 13) and (suit <= 3 and suit >= 0):
			self.rank = rank
			self.suit = suit
		else:
			raise CardException(rank, suit)

	def __repr__(self):
		"""Returns a string of the current card in an easy to read format"""
		return "{} of {}".format(Card.RANK[self.rank], Card.SUIT[self.suit])

	def get_card_value(self):
		if self.rank > 10: #jack, queen and king all worth 10
			return 10
		else:
			return self.rank

#DEBUG
if __name__ == "__main__":
	card = Card(12, 3)
	print(card)
	print(card.get_card_value())